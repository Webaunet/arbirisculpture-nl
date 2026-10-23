# Génère prestations, entreprise, contact, mentions-legales à partir de index.html (en-tête/pied communs).
import re,os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE="https://webaunet.github.io/arbirisculpture-nl/"
src=open(R+"/index.html",encoding="utf-8").read()
i=src.index("<main>");j=src.index("</main>")+7
head=src[:i];foot=src[j:]
head=head.replace('href="index.html" aria-label','href="%s" aria-label'%BASE)
foot=foot
def page(fn,title,desc,cur,body,extra=""):
    h=head
    h=re.sub(r"<title>.*?</title>","<title>%s</title>"%title,h)
    h=re.sub(r'(<meta name="description" content=)"[^"]*"',r'\1"%s"'%desc,h)
    h=h.replace(' aria-current="page"','')
    if cur:
        h=h.replace('href="%s">'%cur,'href="%s" aria-current="page">'%cur)
    else:
        pass
    f=foot
    if extra:f=f.replace("</body>",extra+"\n</body>")
    open(R+"/"+fn,"w",encoding="utf-8").write(h+"<main>\n"+body+"\n</main>"+f)
# ---- accueil : logo absolu
open(R+"/index.html","w",encoding="utf-8").write(src.replace('href="index.html" aria-label','href="%s" aria-label'%BASE))

TEL='<a class="btn btn-p" href="tel:+33678032012">Appeler le 06 78 03 20 12</a>'
# ---- prestations
P='''<section class="phead" aria-labelledby="t-p">
<div class="wrap">
<div>
<span class="eyebrow">Prestations</span>
<h1 id="t-p">Du pied d'arbre à la dernière dalle</h1>
<p class="lead">Arbres, pierre, bois, pelouse : les travaux d'un jardin se préparent ensemble. Voici les domaines dans lesquels Arbirisculpture N.L. peut intervenir.</p>
<div class="actions"><a class="btn btn-p" href="contact.html">Demander un devis</a><a class="btn btn-s" href="tel:+33678032012">Appeler maintenant</a></div>
</div>
<div class="mosaic">
<img src="images/elagage-demontage.jpg" alt="Arboriste grimpeur démontant un arbre au-dessus d'un jardin" width="1000" height="545">
<img src="images/allee-eclairee.jpg" alt="Allée dallée éclairée au crépuscule devant une maison en pierre" width="1000" height="545">
<img src="images/pelouse-entretien.jpg" alt="Pelouse tondue par un robot et massif fleuri devant une maison" width="1000" height="545">
</div>
</div>
</section>

<section class="sec bg-sauge" id="arbres" aria-labelledby="t-arb">
<div class="wrap split">
<div class="photo"><img src="images/taille-reduction-arbre.jpg" alt="Arboriste dans la couronne d'un chêne après une taille de réduction" width="1000" height="545" loading="lazy"></div>
<div>
<span class="eyebrow">Arbres et végétal</span>
<h2 id="t-arb">Travailler avec l'arbre, pas contre lui</h2>
<p>Un arbre est souvent l'élément le plus ancien d'un jardin. Taille, élagage, réduction : l'intervention se décide sur place, en fonction de l'arbre, de son environnement et de ce que vous attendez de lui.</p>
<ul class="check"><li>Évaluation du besoin avant toute intervention</li><li>Travail au sol ou en hauteur selon la configuration du terrain</li><li>Chantier laissé propre à la fin de l'intervention</li></ul>
</div>
</div>
</section>

<section class="sec bg-creme" id="pierre-bois" aria-labelledby="t-pb">
<div class="wrap">
<span class="eyebrow">Pierre, bois et circulations</span>
<h2 id="t-pb">Construire les espaces où l'on vit dehors</h2>
<p>Un jardin se pratique autant qu'il se regarde. Ces trois types d'ouvrages en dessinent les usages.</p>
<div class="trio">
<article class="tcard"><img src="images/terrasse-bois.jpg" alt="Pose d'une terrasse en bois le long d'une maison en pierre" width="1000" height="545" loading="lazy"><div><h3>Terrasses</h3><p>Une terrasse bien placée prolonge la maison : orientation, matériau et niveaux se choisissent avec vous.</p></div></article>
<article class="tcard"><img src="images/allee-dallee-jardin.jpg" alt="Allée en dalles de pierre bordée d'un muret fleuri" width="1000" height="545" loading="lazy"><div><h3>Allées et cheminements</h3><p>Dalles, pavés ou autre revêtement : un tracé simple, durable et agréable à parcourir.</p></div></article>
<article class="tcard"><img src="images/muret-pierre-seche.jpg" alt="Muret en pierre naturelle et escalier autour d'un massif" width="1000" height="545" loading="lazy"><div><h3>Murets et escaliers</h3><p>Pierre naturelle, soutènement, marches : la maçonnerie paysagère qui structure un terrain en pente.</p></div></article>
</div>
</div>
</section>

<section class="bg-sauge" aria-labelledby="t-ent">
<div class="bark">
<div class="wrap split rev">
<div class="photo"><img src="images/pelouse-entretien.jpg" alt="Jardin entretenu avec pelouse rayée et massif en bordure" width="1000" height="545" loading="lazy"></div>
<div>
<span class="eyebrow">Entretien</span>
<h2 id="t-ent">Un jardin réussi se garde en forme</h2>
<p>Création terminée, le travail continue : pelouse, massifs, taille des haies. Un entretien régulier évite les gros chantiers de remise en état.</p>
<p>La fréquence et le contenu des passages se définissent avec vous, selon la taille du jardin et vos envies.</p>
<div class="actions" style="margin-top:1.4em"><a class="btn btn-p" href="contact.html">Parler de mon jardin</a></div>
</div>
</div>
</div>
</section>

<section class="strip" aria-labelledby="t-str">
<div class="wrap strip-in">
<div>
<span class="eyebrow">Avant d'appeler</span>
<h2 id="t-str">Préparez votre devis en trois infos</h2>
<p>Pas besoin de plan précis. Quelques éléments suffisent pour démarrer la conversation.</p>
<div class="actions" style="margin-top:1.2em">TEL<a class="btn btn-v" href="contact.html">Remplir le formulaire</a></div>
</div>
<ul><li>Le type de travaux envisagé</li><li>Votre commune</li><li>Le moment où vous aimeriez intervenir</li></ul>
</div>
</section>'''.replace("TEL",TEL)
page("prestations.html","Prestations | Arbirisculpture N.L. au Vésinet","Prestations d'Arbirisculpture N.L. au Vésinet : arbres, terrasses, allées, murets en pierre et entretien de jardin.","prestations.html",P)

# ---- entreprise
E='''<section class="thead" aria-labelledby="t-e">
<div class="wrap">
<div>
<span class="eyebrow">L'entreprise</span>
<h1 id="t-e">Arbirisculpture N.L., paysagiste au Vésinet</h1>
<p class="lead" style="font-size:1.15rem;margin-top:1em">Une société d'aménagement paysager installée dans les Yvelines, enregistrée depuis le début de l'année 2004. Elle est à votre service pour concevoir, réaliser et entretenir votre jardin.</p>
</div>
<dl class="fiche">
<div><dt>Création</dt><dd>5 janvier 2004</dd></div>
<div><dt>Forme</dt><dd>Société à responsabilité limitée</dd></div>
<div><dt>Siège</dt><dd>Le Vésinet (78110)</dd></div>
<div><dt>Activité</dt><dd>Services d'aménagement paysager</dd></div>
</dl>
</div>
</section>

<section class="sec bg-creme" aria-labelledby="t-a">
<div class="wrap split">
<div>
<span class="eyebrow">Notre approche</span>
<h2 id="t-a">Trois idées pour guider chaque chantier</h2>
<div class="princ" style="grid-template-columns:1fr;margin-top:1.4em;gap:22px">
<div><h3>Partir du lieu</h3><p>Le sol, l'exposition, les arbres déjà présents : le projet se construit sur ce qui existe.</p></div>
<div><h3>Parler clairement</h3><p>Un échange direct, un devis lisible, des explications sans jargon.</p></div>
<div><h3>Penser à la suite</h3><p>Un jardin doit rester agréable et facile à entretenir bien après la fin du chantier.</p></div>
</div>
</div>
<div class="photo" style="aspect-ratio:4/4.6"><img src="images/equipe-materiel-arboriste.jpg" alt="Deux arboristes équipés préparant leur matériel au pied d'un grand arbre" width="1000" height="545" loading="lazy"></div>
</div>
</section>

<section class="sec bg-sauge" aria-labelledby="t-c" style="align-items:center">
<div class="wrap" style="width:min(1120px,100% - 0px)">
<div class="bigtel">
<span class="eyebrow">Nous joindre</span>
<h2 id="t-c" style="margin-bottom:.1em">Le plus simple : un coup de téléphone</h2>
<a class="num" href="tel:+33678032012">06 78 03 20 12</a>
<p>Pour présenter votre projet ou demander un devis pour votre jardin au Vésinet et alentours.</p>
<div class="actions" style="justify-content:center;margin-top:1.4em"><a class="btn btn-p" href="contact.html">Écrire un message</a></div>
</div>
</div>
</section>'''
page("entreprise.html","L'entreprise | Arbirisculpture N.L. au Vésinet","Arbirisculpture N.L. : société d'aménagement paysager créée en 2004, siège au Vésinet (78). Présentation et coordonnées.","entreprise.html",E)

# ---- contact
C='''<section class="thead" aria-labelledby="t-ct">
<div class="wrap" style="display:block">
<span class="eyebrow">Contact</span>
<h1 id="t-ct" style="font-size:clamp(2rem,5vw,3.2rem);margin-bottom:.3em">Parlons de votre jardin</h1>
<p style="max-width:40rem">Appelez directement, ou remplissez le formulaire plus bas : il prépare un message prêt à envoyer par SMS ou à copier.</p>
<div class="cc">
<div class="carte"><span class="eyebrow">Téléphone</span><br><a class="tl" href="tel:+33678032012" style="font-family:Fraunces,Georgia,serif;font-size:1.6rem;font-weight:600;text-decoration:none;display:inline-flex;align-items:center;min-height:48px">06 78 03 20 12</a></div>
<div class="carte"><span class="eyebrow">Adresse du siège</span><p>6 rue du Maréchal Foch<br>78110 Le Vésinet</p></div>
</div>
<div class="actions" style="margin-top:2em"><a class="btn btn-p" href="#devis">Aller au formulaire</a></div>
</div>
</section>

<section class="form-sec" aria-labelledby="t-f">
<div class="wrap">
<form class="form-card" id="devis" novalidate aria-labelledby="t-f">
<h2 id="t-f">Votre demande de devis</h2>
<div class="fld"><label for="nom">Nom</label><input id="nom" name="nom" type="text" autocomplete="name" required aria-describedby="e-nom"><p class="err" id="e-nom" role="alert"></p></div>
<div class="fld"><label for="tel">Téléphone</label><input id="tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" required aria-describedby="e-tel"><p class="err" id="e-tel" role="alert"></p></div>
<div class="fld"><label for="commune">Commune</label><input id="commune" name="commune" type="text" autocomplete="address-level2" required aria-describedby="e-commune"><p class="err" id="e-commune" role="alert"></p></div>
<div class="fld"><label for="besoin">Votre besoin</label><select id="besoin" name="besoin" required aria-describedby="e-besoin"><option value="">Choisir dans la liste</option><option>Création ou rénovation de jardin</option><option>Terrasse ou allée</option><option>Muret ou maçonnerie paysagère</option><option>Taille ou élagage d'arbres</option><option>Entretien régulier du jardin</option><option>Autre demande</option></select><p class="err" id="e-besoin" role="alert"></p></div>
<div class="fld"><label for="message">Message <span class="opt">(facultatif)</span></label><textarea id="message" name="message" rows="4" autocomplete="off"></textarea></div>
<button class="btn btn-p" type="submit">Préparer ma demande</button>
<div class="recap" id="recap" hidden tabindex="-1" aria-live="polite">
<h3>Votre demande est prête</h3>
<p>Aucun message n'est parti pour l'instant. Choisissez comment l'envoyer.</p>
<pre id="recap-txt"></pre>
<div class="actions"><a class="btn btn-p" id="r-sms" href="sms:+33678032012">Envoyer par SMS</a><button class="btn btn-c" id="r-copy" type="button">Copier</button><a class="btn btn-v" href="tel:+33678032012">Appeler</a></div>
<p id="r-ok" role="status" style="margin-top:12px"></p>
</div>
</form>
</div>
</section>'''
page("contact.html","Contact | Arbirisculpture N.L. au Vésinet","Contactez Arbirisculpture N.L., paysagiste au Vésinet (78) : formulaire de demande de devis et téléphone 06 78 03 20 12.","contact.html",C)

# ---- mentions légales
M='''<section class="sec bg-creme" style="min-height:calc(100svh - var(--h));align-items:flex-start" aria-labelledby="t-m">
<div class="wrap legal">
<h1 id="t-m" style="font-size:clamp(2rem,5vw,3rem)">Mentions légales</h1>
<p>Ce site est une maquette de présentation. Il ne constitue pas le site officiel de l'entreprise.</p>
<h2>Entreprise</h2>
<dl>
<dt>Dénomination</dt><dd>ARBIRISCULPTURE N.L.</dd>
<dt>Forme juridique</dt><dd>Société à responsabilité limitée</dd>
<dt>SIREN</dt><dd>451 404 586</dd>
<dt>Siège social</dt><dd>6 rue du Maréchal Foch, 78110 Le Vésinet</dd>
<dt>Activité</dt><dd>Services d'aménagement paysager</dd>
<dt>Téléphone</dt><dd><a href="tel:+33678032012">06 78 03 20 12</a></dd>
</dl>
<h2>Hébergement</h2>
<p>Maquette hébergée sur GitHub Pages (GitHub, Inc.).</p>
<h2>Données personnelles</h2>
<p>Le formulaire de contact fonctionne dans votre navigateur : les informations saisies ne sont ni envoyées ni enregistrées par ce site.</p>
<div class="note"><p><strong>À compléter par l'entreprise :</strong> directeur de la publication, adresse e-mail de contact, numéro de TVA le cas échéant.</p></div>
</div>
</section>'''
page("mentions-legales.html","Mentions légales | Arbirisculpture N.L. au Vésinet","Mentions légales de la maquette du site d'Arbirisculpture N.L., société d'aménagement paysager au Vésinet (78).","",M)
print("ok")
