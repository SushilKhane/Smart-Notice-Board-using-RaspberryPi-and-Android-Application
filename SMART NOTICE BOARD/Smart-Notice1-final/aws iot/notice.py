a.V=d);ntp_Dl(a,b);var d=b.nd,f=b.Jd;if(a.o&&a.T)if(d){var g=ntp_J(a.W);g||(g=new Image,g.id=a.W,a.o.appendChild(g));ntp_O(g,"content",d);a.o.classList.toggle("left-align-attr","right"===f);a.o&&ntp_lf(a.o,!0)}else a.o&&ntp_lf(a.o,!1);if(d=!1!==b.md&&e)b.imageUrl?d=!1:(d=ntp_El(b),d=9>Math.max(d[0],d[1],d[2])-Math.min(d[0],
d[1],d[2])),d=!d;d?a.H.render(1):a.H.render(0);d=!1;!ntp_Al(a)&&e&&ntp_Fl(b)&&(d=!0);ntp_Gl(d);a.R=c}}}},ntp_Cl=function(a){return[a.Na?ntp_Hl(a.Na):a.Xa,a.imageUrl,a.Kd,a.Jd,a.Ld].join(" ").trim()},ntp_Bl=function(a){document.body.style.background="";ntp_Gl(!1);ntp_Dl(a);a.o&&ntp_lf(a.o,!1)},ntp_Hl=function(a){return"rgba("+a[0]+","+a[1]+","+a[2]+","+a[3]/255+")"},ntp_Dl=function(a,b){var c=ntp_J("ctStyle");c&&ntp_Ne(c);if(b&&!b.Vb){var c="color:#fff !important;text-shadow:black 0 1px 3px !important",
d="color:#fff !important;text-shadow:#1155cc 0 1px 3px !important",e="color:#fff;text-shadow:black 0 1px 3px";b.Eb&&(c="color:"+ntp_Hl(b.Eb)+" !important");b.Ub&&(d="color:"+ntp_Hl(b.Ub)+" !important",e="color:"+ntp_Hl(b.Ub)+";");c=["#body a,#footer a,#footer>span,","#prm,","#als,","#gbi4t,",".sblc a,",".mv-title,","#mv-noti-msg,","#mv-noti-error-msg{",c,"}","#prm a,","#alp-link,","#mv-noti-lks span,","#mv-noti-error-lks span{",d,"}","#theme-attr-msg{",e,"}","#sbl,#fctr,.fade{background:transparent}",
".gbh{border:none}","body{background-attachment:fixed!important}"];b.Eb&&c.push("#mv-noti-x{-webkit-filter:drop-shadow(0 0 0 "+ntp_Hl(b.Eb)+")}");b.Wc&&b.Ac&&c.push(".des-cla .mv-tile .mv-mask,",".des-mat .mv-tile .mv-mask{","border:1px solid ",ntp_Hl(b.Wc),"}",".des-cla .mv-page:hover .mv-mask,",".des-mat .mv-page:hover .mv-mask,",".des-cla .mv-page .mv-focused ~ .mv-page .mv-mask,",".des-mat .mv-page .mv-focused ~ .mv-page .mv-mask,",".des-cla .mv-page:focus .mv-mask,",".des-mat .mv-page:focus .mv-mask{",
"border:1px solid ",ntp_Hl(b.Ac),"}");c=c.join("");c=ntp_Y("STYLE",{id:"ctStyle",type:"text/css"},c+a.H.U);document.body.appendChild(c);document.body.classList.remove("default-theme")}else document.body.classList.add("default-theme");document.body.classList.toggle("light-text",b?ntp_Il(b):!1)},ntp_Gl=function(a){window.gbar&&window.gbar.tst&&window.gbar.tst(a?"dark":"default")},ntp_Al=function(a){try{var b=a.ha.get("esp-st");return!!b&&!isNaN(b)&&!!parseInt(b,10)}catch(c){}return!1};
ntp_xl.prototype.wa=function(){try{this.ha.set("esp-st","1")}catch(a){}ntp_Bl(this);this.H.render(0);this.U()};ntp_xl.prototype.ta=function(){var a=ntp_gl();if(!a||ntp_Al(this))return!0;a=ntp_Cl(a);return!(a&&-1==ntp_zl.indexOf(a))};
var ntp_El=function(a){if(a.Na&&4==a.Na.length)return a.Na;if(a.Xa){var b,c;try{re