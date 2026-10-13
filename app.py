import streamlit as st
from pathlib import Path
import random, re

st.set_page_config(page_title="Isi's Cocktailbar | 40 & Fabulous",page_icon="🍸",layout="wide",initial_sidebar_state="collapsed")
st.markdown('''<style>@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Inter:wght@400;600&display=swap');html,body,[class*="css"],.stApp{font-family:Inter,sans-serif}.stApp{background:linear-gradient(140deg,#12100f,#221c18 48%,#100e0d);color:#f5eadc}h1,h2,h3{font-family:'Playfair Display',serif!important;color:#e8c78b!important}.stButton>button{border:1px solid #be9c62;border-radius:14px;background:#2a211b;color:#f6e7c9;width:100%;min-height:3rem}.stButton>button:hover{background:#71552f;color:white}.block-container{padding-top:1rem;max-width:1130px}div[data-testid="stMetric"]{background:#251e19;border-radius:14px;padding:12px}div[data-testid="stVerticalBlockBorderWrapper"]{border-color:#685237!important}.stSelectbox label,.stMultiSelect label{color:#edd9ae!important}.subtitle{color:#dfc695;text-align:center;letter-spacing:2px}.title{text-align:center;font-size:clamp(2.5rem,7vw,5.4rem);font-family:'Playfair Display',serif;color:#e8c78b;line-height:1.05}.chip{color:#e2ceab;font-size:.92em}.fine{color:#cabba5;font-size:.85em}</style>''',unsafe_allow_html=True)

NAMES=['7 & 7','Ambassador','Appletini','B-52','Bacardi Cocktail',"Bee’s Knees",'Between The Sheets','Black Russian','Blue Kamikaze','Blue Lagoon','Boilermaker','Boilermaker (Fortsetzung)','Brandy Egg Nogg','Brandy Separator','Brave Bull',"Buck’s Fizz",'Bumbo','Caipirinha','Cape Cod','Clover Club','Colorado Bulldog','Cosmopolitan','Cuba Libre','Culo A La Vida','Daiquiri','French 75','Gimlet','Gin and Sin','Gin Fizz','Gin Rickey','Highball','Horny Bull (long)','Horny Bull (shot)','Hot Toddy','Jack and Coke','John Collins','Kamikaze','Kir','Kir Royale','Lemon Drop','Long Beach Iced Tea','Long Island Iced Tea','Margarita','Martini Espresso','Martini Lemon Drop','Mimosa','Mint Julep','Mojito','Monkey Gland','Mudslide','New York Sour','Pink Lady','Rickey Cocktails','Russian Spring Punch','Screwdriver','Sidecar','Silver Bullet','Sneaky Pete','Southside','Southside (Variante)','Spritz Veneziano','Tequila Slammer','Tequila Sunrise','Tootsie Roll','Ward 8','Whisky Sour','White Lady','Mai Tai','Bay Breeze','Pina Colada']
# Ingredients: (name, ml per cocktail; 0 means unit/optional listed as a textual garnish)
RAW={
'Margarita':('Tequila', [('Tequila',50),('Triple Sec',30),('Limettensaft',20)],'Sauer · frisch','Alle flüssigen Zutaten mit Eis kräftig shaken. In ein Glas mit Salzrand abseihen. Limette garnieren.','Shaker · Cocktailglas'),
'Mojito':('Rum',[('Weißer Rum',50),('Limettensaft',25),('Sodawasser',80),('Zuckersirup',15)],'Frisch · minzig','Minze und Limettenstücke sanft mit Zucker andrücken. Rum und Eis ergänzen, mit Soda auffüllen, vorsichtig verrühren.','Highball · Minze · Limette'),
'Cosmopolitan':('Wodka',[('Wodka',40),('Cointreau',15),('Cranberrysaft',30),('Limettensaft',15)],'Fruchtig · sauer','Mit Eis kräftig shaken und in ein vorgekühltes Cocktailglas doppelt abseihen.','Cocktailglas · Orangenzeste'),
'Pina Colada':('Rum',[('Weißer Rum',50),('Kokoscreme',30),('Ananassaft',90)],'Cremig · tropisch','Mit Crushed Ice kräftig shaken oder kurz mixen. In ein hohes Glas geben.','Hurricane · Ananas'),
'Daiquiri':('Rum',[('Weißer Rum',50),('Limettensaft',25),('Zuckersirup',15)],'Sauer · klassisch','Mit Eis kräftig shaken und in ein gekühltes Glas abseihen.','Coupette'),
'Cuba Libre':('Rum',[('Weißer Rum',50),('Cola',120),('Limettensaft',15)],'Süß · erfrischend','Eis in ein Longdrinkglas geben, Rum und Limette dazu, mit Cola auffüllen.','Longdrink · Limette'),
'Tequila Sunrise':('Tequila',[('Tequila',45),('Orangensaft',90),('Grenadine',15)],'Fruchtig · süß','Tequila und Orangensaft auf Eis geben. Grenadine langsam einlaufen lassen – nicht umrühren.','Highball · Orange'),
'Appletini':('Wodka',[('Wodka',45),('Apfellikör',30),('Cointreau',15)],'Fruchtig · spritzig','Zutaten mit Eis shaken und in ein gekühltes Cocktailglas abseihen.','Cocktailglas · Apfelscheibe'),
'Blue Lagoon':('Wodka',[('Wodka',40),('Blue Curaçao',20),('Zitronenlimonade',120)],'Fruchtig · süß','Wodka und Blue Curaçao auf Eis geben, mit Zitronenlimonade auffüllen.','Highball'),
'Black Russian':('Wodka',[('Wodka',50),('Kaffeelikör',25)],'Kräftig · Kaffee','Über Eis direkt im Tumbler verrühren.','Tumbler'),
'White Lady':('Gin',[('Gin',40),('Triple Sec',30),('Zitronensaft',20)],'Sauer · elegant','Mit Eis shaken und in ein gekühltes Glas abseihen.','Cocktailglas'),
'Gin Fizz':('Gin',[('Gin',45),('Zitronensaft',25),('Zuckersirup',15),('Sodawasser',80)],'Frisch · sauer','Gin, Zitrone und Sirup mit Eis shaken, abseihen und mit Soda auffüllen.','Highball'),
'Gimlet':('Gin',[('Gin',60),('Limettensaft',25),('Zuckersirup',15)],'Sauer · herb','Mit Eis shaken und in eine Coupette abseihen.','Coupette'),
'French 75':('Gin',[('Gin',30),('Zitronensaft',15),('Zuckersirup',10),('Sekt',80)],'Spritzig · festlich','Gin, Zitrone und Sirup shaken, in eine Sektflöte abseihen und mit Sekt auffüllen.','Sektflöte'),
'Mimosa':('Sekt',[('Sekt',75),('Orangensaft',75)],'Fruchtig · leicht','Gut gekühlte Zutaten behutsam in einer Sektflöte zusammengeben.','Sektflöte'),
'Spritz Veneziano':('Sekt',[('Sekt',90),('Aperol',60),('Sodawasser',30)],'Herb · spritzig','Weinglas mit Eis füllen. Sekt, Aperol, Soda zugeben und vorsichtig verrühren.','Weinglas · Orangenscheibe'),
'Mai Tai':('Rum',[('Weißer Rum',40),('Dunkler Rum',20),('Triple Sec',15),('Limettensaft',25),('Mandelsirup',15)],'Tropisch · kräftig','Alle Zutaten mit Eis shaken, in einen Tumbler mit Crushed Ice geben.','Tumbler · Minze'),
'Espresso Martini':('Wodka',[('Wodka',50),('Kaffeelikör',20),('Espresso',30),('Zuckersirup',10)],'Kaffee · intensiv','Frischen, abgekühlten Espresso mit übrigen Zutaten und viel Eis sehr kräftig shaken; fein abseihen.','Cocktailglas · Kaffeebohnen'),
'Martini Espresso':('Wodka',[('Wodka',50),('Kaffeelikör',20),('Espresso',30),('Zuckersirup',10)],'Kaffee · intensiv','Alle Zutaten mit Eis sehr kräftig shaken und abseihen.','Cocktailglas · Kaffeebohnen'),
'Whisky Sour':('Whisky',[('Whisky',60),('Zitronensaft',30),('Zuckersirup',15)],'Sauer · kräftig','Mit Eis shaken, über frischem Eis servieren. Optional mit pasteurisiertem Eiweiß für Schaum.','Tumbler · Zitronenzeste'),
'New York Sour':('Whisky',[('Whisky',60),('Zitronensaft',25),('Zuckersirup',15),('Rotwein',15)],'Sauer · fruchtig','Whisky, Zitrone und Sirup shaken, auf Eis abseihen; Rotwein vorsichtig darüber floaten.','Tumbler'),
'Screwdriver':('Wodka',[('Wodka',50),('Orangensaft',120)],'Fruchtig · einfach','Wodka und Orangensaft auf Eis ins Glas geben, leicht umrühren.','Highball'),
'Cape Cod':('Wodka',[('Wodka',45),('Cranberrysaft',120),('Limettensaft',15)],'Fruchtig · frisch','Auf Eis bauen und leicht verrühren.','Highball'),
'Kamikaze':('Wodka',[('Wodka',30),('Triple Sec',30),('Limettensaft',30)],'Sauer · kräftig','Mit Eis kräftig shaken und in ein gekühltes Glas abseihen.','Cocktailglas'),
'Long Island Iced Tea':('Mehrere',[('Wodka',15),('Tequila',15),('Weißer Rum',15),('Gin',15),('Triple Sec',15),('Zitronensaft',25),('Cola',60)],'Kräftig · süß','Alle Zutaten außer Cola mit Eis shaken, in ein Longdrinkglas abseihen, mit Cola auffüllen.','Highball · Achtung: alkoholstark'),
'Long Beach Iced Tea':('Mehrere',[('Wodka',15),('Tequila',15),('Weißer Rum',15),('Triple Sec',15),('Cranberrysaft',90)],'Fruchtig · kräftig','Mit Eis shaken und in ein Longdrinkglas geben.','Longdrink'),
'Caipirinha':('Cachaça',[('Cachaça',50),('Limettensaft',25),('Zuckersirup',15)],'Sauer · frisch','Limettenachtel mit Zucker leicht andrücken, Cachaça und Crushed Ice zugeben.','Tumbler · Limette'),
'Kir Royale':('Sekt',[('Crème de Cassis',10),('Sekt',90)],'Beerig · elegant','Cassis in die Sektflöte geben und mit gekühltem Sekt auffüllen.','Sektflöte'),
'Mudslide':('Wodka',[('Wodka',30),('Kaffeelikör',30),('Irish Cream',30)],'Cremig · süß','Mit Eis shaken und in einem Tumbler auf Eis servieren.','Tumbler'),
'Bay Breeze':('Wodka',[('Wodka',40),('Cranberrysaft',90),('Ananassaft',60)],'Fruchtig · leicht','Auf Eis ins Longdrinkglas geben und verrühren.','Highball'),
'Sidecar':('Cognac',[('Cognac',50),('Cointreau',20),('Zitronensaft',20)],'Sauer · elegant','Mit Eis shaken und in eine gekühlte Coupette abseihen.','Coupette'),
'Moscow Mule':('Wodka',[('Wodka',50),('Limettensaft',20),('Ginger Beer',120)],'Würzig · erfrischend','Auf Eis bauen, mit Ginger Beer auffüllen und kurz verrühren.','Becher · Limette'),
}
# Every screenshot is retained and selectable, even if typed transcription is not yet confirmed.
files=sorted(Path(__file__).parent.joinpath('screenshots').glob('*.jpg'))
assert len(files)==len(NAMES),f'{len(files)} images vs {len(NAMES)} names'
records=[]
for i,(name,path) in enumerate(zip(NAMES,files)):
 key='Espresso Martini' if name=='Martini Espresso' else name
 data=RAW.get(key)
 if data: base,ings,taste,method,glass=data
 else: base,ings,taste,method,glass='Original-Screenshot',[], 'Originalrezept','Die vollständige Zutatenliste und Zubereitung stehen im Original-Screenshot unten.','Originalrezept'
 records.append(dict(name=name,base=base,ingredients=ings,taste=taste,method=method,glass=glass,image=path,verified=bool(data)))

st.markdown('<p class="subtitle">PRIVATE BIRTHDAY EDITION · 17.10.2026</p><div class="title">Isi’s Cocktailbar 🍸</div><p class="subtitle">FORTY & FABULOUS · MIX YOUR MAGIC</p>',unsafe_allow_html=True)
st.write('')
st.caption('Wähle deinen Lieblingsdrink – oder lass dich überraschen. Santé, Isi! 🥂')
a,b=st.columns([2,1]);
with a: spirit=st.multiselect('🍾 Basisspirituose',sorted({r['base'] for r in records if r['base']!='Original-Screenshot'}),placeholder='Alle Cocktails anzeigen')
with b: search=st.text_input('🔎 Cocktail suchen',placeholder='z. B. Mojito')
all_ingredients=sorted({n for r in records for n,v in r['ingredients']});picked=st.multiselect('🧊 Zutaten, die du verwenden möchtest (optional)',all_ingredients,placeholder='Zutaten auswählen')
only_ready=st.toggle('Nur vollständig übertragene Rezepte',value=False)
matched=[r for r in records if (not search or search.lower() in r['name'].lower()) and (not spirit or r['base'] in spirit or (r['base']=='Mehrere' and any(any(s.lower() in n.lower() for n,v in r['ingredients']) for s in spirit))) and (not picked or all(x in [n for n,v in r['ingredients']] for x in picked)) and (not only_ready or r['verified'])]
cols=st.columns([2,1,1]);cols[0].metric('Cocktails zur Auswahl',len(matched));cols[1].metric('Original-Screenshots',len(files));cols[2].metric('Rezepttexte',sum(r['verified'] for r in records))
if st.button('🎲 Surprise me, Isi!',use_container_width=True):
 if matched: st.session_state['chosen']=random.choice(matched)['name']
if 'chosen' not in st.session_state: st.session_state['chosen']=None
st.markdown('### Deine Cocktailkarte')
if not matched: st.info('Kein passender Cocktail. Wähle weniger Filter.')
else:
 for chunk in [matched[i:i+3] for i in range(0,len(matched),3)]:
  c=st.columns(3)
  for col,r in zip(c,chunk):
   with col:
    with st.container(border=True):
     st.markdown(f"#### {r['name']}")
     st.markdown(f"<p class='chip'>{r['taste']} · {r['base']}</p>",unsafe_allow_html=True)
     if st.button('Rezept öffnen →',key='open_'+str(r['image'])):st.session_state['chosen']=r['name'];st.rerun()
chosen=next((r for r in records if r['name']==st.session_state.get('chosen')),None)
if chosen:
 st.divider();st.markdown('## 🍹 '+chosen['name'])
 left,right=st.columns([1,1.15])
 with left:
  st.image(str(chosen['image']),caption='Originalrezept (Archiv-Screenshot)',use_container_width=True)
 with right:
  if chosen['verified']:
   servings=st.number_input('Anzahl Cocktails',min_value=1,max_value=30,value=1,step=1)
   st.markdown('#### Zutaten')
   for n,v in chosen['ingredients']:st.write(f'**{v*servings:g} ml**  {n}')
   st.markdown('#### Zubereitung');st.write(chosen['method']);st.caption(chosen['glass'])
   st.info('Die Textfassung ist eine praxistaugliche Rezeptvariante. Für die Mengen aus der ursprünglichen Sammlung siehe den Original-Screenshot.')
  else:
   st.warning('Dieser Cocktail ist über den Original-Screenshot verfügbar; Zutaten und Schritte wurden noch nicht zuverlässig in Text übertragen.')
   st.write(chosen['method'])
 st.button('↑ Zur Cocktailauswahl',on_click=lambda:st.session_state.update(chosen=None))
st.divider();st.caption('Isi’s Cocktailbar · Mit Liebe für einen besonderen 40er gemacht · Bitte verantwortungsvoll genießen. 🍸')
