import streamlit as st
import json, random, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
RECIPES=json.loads((ROOT/'recipes.json').read_text(encoding='utf-8'))
SPIRITS=['Wodka','Gin','Rum','Tequila','Whisky','Bourbon','Cognac','Brandy','Cachaça','Sekt / Prosecco','Aperol','Andere Liköre']

def show_photo(recipe):
    photo=ROOT/'assets'/f"photo_{recipe['id']:02d}.svg"
    if photo.exists():st.image(photo.read_text(encoding='utf-8'),use_container_width=True)

def spirit_tags(recipe):
    blob=' '.join(x['ingredient'].lower() for x in recipe['ingredients'])
    tags=[]
    match={'Wodka':('wodka','vodka'),'Gin':('gin',),'Rum':('rum',),'Tequila':('tequila',),'Whisky':('whisky','whiskey','jack daniel','roggenwhisky','scotch','bourbon'),'Bourbon':('bourbon',),'Cognac':('cognac',),'Brandy':('brandy',),'Cachaça':('cachaça','cachaca'),'Sekt / Prosecco':('sekt','prosecco','champagner'),'Aperol':('aperol',),'Andere Liköre':('likör','kahlúa','kahlua','cointreau','triple sec','curaçao','baileys','crème de cassis','apfelschnaps','absinth')}
    for tag,terms in match.items():
        if any(re.search(r'(?<!\w)' + re.escape(term) + r'(?!\w)', blob) for term in terms):tags.append(tag)
    return tags

def ingredient_display(row, servings):
    qty=row.get('qty','').strip(); unit=row.get('unit','').strip(); name=row['ingredient']
    try:
        n=float(qty.replace(',','.'))*servings
        value=f'{n:g}'.replace('.',',')
    except (ValueError,TypeError):
        value=qty
    if not value and not unit:return name + (' · nach Bedarf' if any(word in row.get('note','').lower() for word in ['auffüll','menge nicht']) else '')
    return f'{value} {unit} {name}'.strip()

st.set_page_config(page_title="Isi’s Cocktailbar | Forty & Fabulous",page_icon='🍸',layout='wide',initial_sidebar_state='collapsed')
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');
.stApp{background:radial-gradient(ellipse at top,#30201e 0,#171316 42%,#0e0c0e 100%);color:#f5e9db;font-family:Inter,sans-serif}
h1,h2,h3{font-family:'Playfair Display',serif!important;color:#ebcc90!important}
.block-container{max-width:1120px;padding-top:1.2rem} .stButton>button{border:1px solid #99794c;border-radius:14px;background:#302522;color:#f7e4c4;min-height:2.8rem;width:100%}.stButton>button:hover{background:#6b4a31;color:white}
.hero{text-align:center;padding:1.5rem 0 1rem}.eyebrow{color:#d7b77a;text-transform:uppercase;letter-spacing:.21rem;font-size:.72rem}.hero-title{font-family:'Playfair Display',serif;font-size:clamp(2.4rem,8vw,5rem);color:#e8c789;line-height:1.09}.hero-sub{font-size:1rem;color:#d9c9b6;margin-top:.8rem}
.small{color:#c5b5a3;font-size:.88rem}.gold{color:#d9bd81}.stImage img{border-radius:14px}
</style>""",unsafe_allow_html=True)
st.markdown('<div class="hero"><div class="eyebrow">17. Oktober 2026 · 40 & Fabulous</div><div class="hero-title">Isi’s Cocktailbar 🍸</div><div class="hero-sub">Dein Drink. Dein Moment. Auf Isi! 🥂</div></div>',unsafe_allow_html=True)

if 'selected' not in st.session_state: st.session_state.selected=None
if 'surprise_id' not in st.session_state: st.session_state.surprise_id=None
if 'scroll_token' not in st.session_state: st.session_state.scroll_token=0
if 'scroll_pending' not in st.session_state: st.session_state.scroll_pending=False
if 'return_to_id' not in st.session_state: st.session_state.return_to_id=None
if 'return_scroll_token' not in st.session_state: st.session_state.return_scroll_token=0

a,b=st.columns([1,1])
with a: selected_spirits=st.multiselect('🍾 Spirituosen auswählen',SPIRITS,placeholder='Alle Spirituosen')
with b: term=st.text_input('🔎 Cocktail suchen',placeholder='z. B. Mojito')
all_ingredients=sorted(set(r['ingredient'] for recipe in RECIPES for r in recipe['ingredients']),key=str.casefold)
chosen_ingredients=st.multiselect('🧊 Zutaten (optional)',all_ingredients,placeholder='Beliebige Zutaten auswählen')
selection_mode=st.radio('Auswahl der Zutaten', ['Enthält alle ausgewählten Zutaten','Enthält mindestens eine'],horizontal=True,label_visibility='collapsed') if len(chosen_ingredients)>1 else 'Enthält alle ausgewählten Zutaten'

def matches(recipe):
    if term.strip() and term.casefold() not in recipe['name'].casefold():return False
    if selected_spirits and not any(t in spirit_tags(recipe) for t in selected_spirits):return False
    found={x['ingredient'] for x in recipe['ingredients']}
    if chosen_ingredients and (not all(x in found for x in chosen_ingredients) if selection_mode.startswith('Enthält alle') else not any(x in found for x in chosen_ingredients)):return False
    return True

matched=[r for r in RECIPES if matches(r)]
if st.button('🎲 Surprise me, Isi!'):
    if matched:
        alternatives=[r for r in matched if r['id']!=st.session_state.selected]
        surprise=random.choice(alternatives or matched)
        st.session_state.selected=surprise['id']
        st.session_state.surprise_id=surprise['id']
    else:st.info('Bitte zuerst deine Filter anpassen.')

rec=next((r for r in RECIPES if r['id']==st.session_state.selected),None)
if rec:
    if st.session_state.surprise_id==rec['id']:
        st.success(f"🎲 Deine Überraschung: {rec['name']}")
    st.divider()
    if st.session_state.scroll_pending:
        target=f"isi-recipe-top-{st.session_state.scroll_token}"
        st.html(
            f'<div id="{target}" style="height:0;scroll-margin-top:96px"></div>'
            '<script>requestAnimationFrame(() => requestAnimationFrame(() => {'
            f'document.getElementById("{target}")?.scrollIntoView({{behavior:"auto",block:"start"}});'
            '}));</script>',
            unsafe_allow_javascript=True,
        )
        st.session_state.scroll_pending=False
    st.markdown(f"## 🍹 {rec['name']}")
    left,right=st.columns([1,1.15],gap='large')
    with left:
        show_photo(rec)
        info_svg=ROOT/'assets'/f"info_{rec['id']:02d}.svg"
        if info_svg.exists():
            st.caption('Über diesen Cocktail')
            st.image(info_svg.read_text(encoding='utf-8'),use_container_width=True)
    with right:
        servings=st.number_input('🍹 Anzahl Cocktails',min_value=1,max_value=30,value=1,step=1,key=f"servings_{rec['id']}")
        st.markdown('#### Zutaten')
        for row in rec['ingredients']:
            st.markdown('- '+ingredient_display(row,servings))
        st.markdown('#### Zubereitung')
        if servings>1:
            st.caption('Die Schritte unten beschreiben einen Cocktail. Für mehrere Cocktails gelten die berechneten Mengen in der Zutatenliste oben.')
        for ix,step in enumerate(rec['steps'],1):st.markdown(f'**{ix}.** {step}')
        st.caption('Mengen werden für die gewünschte Anzahl skaliert. Bei Alternativen jeweils nur eine Variante verwenden. Eis, Garnitur und optionale Zutaten bitte zusätzlich nach Anleitung beachten.')
        if rec['name']=='B-52': st.warning('Sicherheit: Brennende Getränke niemals trinken. Vor dem Trinken vollständig löschen und abkühlen lassen; am besten auf das Entzünden verzichten.')
        if rec['name']=='Tequila Slammer':st.info('Gläser nicht auf harte Oberflächen schlagen: Verletzungs- und Glasbruchgefahr.')
    if st.button('← Cocktailauswahl'):
        st.session_state.return_to_id=rec['id']
        st.session_state.return_scroll_token+=1
        st.session_state.selected=None
        st.session_state.surprise_id=None
        st.rerun()

st.markdown('### Cocktailkarte')
if not matched:st.info('Keine passenden Cocktails gefunden. Bitte Filter anpassen.')
for off in range(0,len(matched),3):
    cols=st.columns(3)
    for col,recipe in zip(cols,matched[off:off+3]):
        with col:
            if st.session_state.return_to_id==recipe['id']:
                target=f"isi-card-{recipe['id']}-{st.session_state.return_scroll_token}"
                st.html(
                    f'<div id="{target}" style="height:0;scroll-margin-top:96px"></div>'
                    '<script>requestAnimationFrame(() => requestAnimationFrame(() => {'
                    f'document.getElementById("{target}")?.scrollIntoView({{behavior:"auto",block:"start"}});'
                    '}));</script>',
                    unsafe_allow_javascript=True,
                )
                st.session_state.return_to_id=None
            with st.container(border=True):
                show_photo(recipe)
                st.markdown(f"#### {recipe['name']}")
                label=' · '.join(spirit_tags(recipe)[:3]) or 'Cocktail'
                st.caption(label)
                if st.button('Rezept ansehen →',key=f"open_{recipe['id']}"):
                    st.session_state.selected=recipe['id']
                    st.session_state.surprise_id=None
                    st.session_state.scroll_token+=1
                    st.session_state.scroll_pending=True
                    st.rerun()
st.divider();st.caption('Isi’s Cocktailbar · Mit Liebe zu deinem 40er · Bitte verantwortungsvoll genießen. 🍸')

