(function(){
var b=document.querySelector('.burger'),m=document.getElementById('menu');
if(!b||!m)return;
function close(){m.classList.remove('open');b.setAttribute('aria-expanded','false');b.setAttribute('aria-label','Ouvrir le menu')}
b.addEventListener('click',function(){
var o=m.classList.toggle('open');
b.setAttribute('aria-expanded',o?'true':'false');
b.setAttribute('aria-label',o?'Fermer le menu':'Ouvrir le menu');
});
m.addEventListener('click',function(e){if(e.target.closest('a'))close()});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m.classList.contains('open')){close();b.focus()}});
window.addEventListener('resize',function(){if(window.innerWidth>980)close()});
})();
(function(){
var f=document.getElementById('devis');
if(!f)return;
var TEL='+33678032012';
function v(id){return f.elements[id].value.trim()}
function err(id,msg){
var e=document.getElementById('e-'+id),i=f.elements[id];
e.textContent=msg;
if(msg){i.setAttribute('aria-invalid','true')}else{i.removeAttribute('aria-invalid')}
return !msg;
}
function check(){
var ok=true,first=null;
function t(id,msg){var r=err(id,msg);if(!r&&!first)first=f.elements[id];ok=ok&&r}
t('nom',v('nom').length<2?'Indiquez votre nom.':'');
var d=v('tel').replace(/[\s.\-()]/g,'');
t('tel',!d?'Indiquez votre numéro de téléphone.':(/^(\+33|0033|0)[1-9]\d{8}$/.test(d)?'':'Numéro invalide. Exemple : 06 12 34 56 78.'));
t('commune',v('commune').length<2?'Indiquez votre commune.':'');
t('besoin',!v('besoin')?'Choisissez votre besoin dans la liste.':'');
if(first)first.focus();
return ok;
}
['nom','tel','commune','besoin'].forEach(function(id){
f.elements[id].addEventListener('input',function(){if(f.elements[id].getAttribute('aria-invalid'))check()});
f.elements[id].addEventListener('change',function(){if(f.elements[id].getAttribute('aria-invalid'))check()});
});
f.addEventListener('submit',function(e){
e.preventDefault();
if(!check())return;
var txt='Bonjour, je souhaite un devis.\nBesoin : '+v('besoin')+'\nNom : '+v('nom')+'\nTéléphone : '+v('tel')+'\nCommune : '+v('commune')+(v('message')?'\nMessage : '+v('message'):'');
var r=document.getElementById('recap');
document.getElementById('recap-txt').textContent=txt;
document.getElementById('r-sms').setAttribute('href','sms:'+TEL+'?&body='+encodeURIComponent(txt));
document.getElementById('r-ok').textContent='';
r.hidden=false;r.focus();
r.scrollIntoView({behavior:'smooth',block:'nearest'});
});
document.getElementById('r-copy').addEventListener('click',function(){
var txt=document.getElementById('recap-txt').textContent,ok=document.getElementById('r-ok');
function fb(){var s=window.getSelection(),g=document.createRange();g.selectNodeContents(document.getElementById('recap-txt'));s.removeAllRanges();s.addRange(g);ok.textContent='Texte sélectionné : copiez-le avec Ctrl+C.'}
if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(function(){ok.textContent='Demande copiée.'},fb)}else{fb()}
});
})();
