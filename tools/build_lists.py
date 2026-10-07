# Builds the files under lists/ from the entries below.
# Usage: python tools/build_lists.py YYYY-MM-DD
import os, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = sys.argv[1]
HOME = 'https://github.com/pedro-nsy/nsy-dns-blocklist'
LISTS = {
 'vpn-proxy': ('VPN and proxy apps',
   'Domains of VPN, proxy and anonymizer apps and services: the well-known brands, the small mobile VPN apps we found in real traffic that the big public lists did not carry when we found them, the publisher families behind them, and the IP-check services the apps use to verify their exit.',
   [
    ('Well-known services', ['protonvpn.com','protonvpn.ch','vpn-api.proton.me','surfshark.com','tunnelbear.com','superunlimited.com','mullvad.net','sec-tunnel.com','nordvpn.com','nordcdn.com','expressvpn.com','windscribe.com','hotspotshield.com','anchorfree.com','cyberghostvpn.com','privateinternetaccess.com','hide.me','hidemyass.com','zenmate.com','betternet.co','psiphon.ca','psiphon3.com','cloudflareclient.com','getoutline.org','ivpn.net','purevpn.com','vyprvpn.com','torguard.net','atlasvpn.com','ultrasurf.us','lantern.io','getlantern.org','torproject.org','x-vpn.com','turbovpn.co','vpnproxymaster.com','hola.org','holavpn.net','urban-vpn.com','browsec.com','speedify.com']),
    ('Small mobile VPN apps and their backends, seen in real traffic', ['luxvpn.cc','vpnlux.cc','vpnrapid.net','thundervpn.net','thundervpnwin.com','free-signal.com','melonvpn.com','suinfra.com','ourip.info','mobilejump.mobi','gofastvpn.com','starwayvpn.xyz','astravpn.xyz','funsol.cloud','bolt-backup.matee-b04.workers.dev','vpnpremiums.com','us-central1-vpn-platform-prod.cloudfunctions.net','tumogle.tech','bytegle.tech','news-cdn.site','apgdmsiifk.com','rateyourispprovider.com','signallab.org','keysuccess.site','securestartup.business','prebreeze.club','cyberanalytics.link','graphlist.dev','zigzagwand.art','vpn2ww.com','vpnlumos.com']),
    ('Sister apps of the families above, from their store pages and public app traffic data (AppGoblin)', ['matrixmobile.net','freevpnapp.net','vpnmelon.com','securesignal.app','alarmpushes.com','fastv.mobi']),
    ("Proton VPN (from Proton's own app source on GitHub: alternative-routing bootstrap, download host, server names)", ['protonpro.xyz','protondownload.com','protonvpn.net']),
    ('VPN app families behind the small apps (publisher sites, the FOCI 2025 paper, app store pages)', ['inconnecting.com','turbovpn.com','secureguardpro.com','materialsofpro.com','snapillustrates.com','autumnbreeze.co','signalsecurevpn.com','xvpn.io','potatovpn.io','freeconnectedlimited.com','vpnsuper.com','unlimitedvpn.im','hvnstore.com','surfsharkstatus.com','uymgg1.com','sir90hl.com','s0r4nd0m.com','hsselite.com','northghost.com','aura-servers.com','cloudflare-gateway.com','cloudflareportal.com','cloudflareok.com','cloudflarecp.com','zerotier.com','psiphon-conduit.com','bright-sdk.com','h-cdn.com','holax.io','opera-proxy.net','alohabrowser.com','alohaprofile.com']),
    ('VPN app backends seen in real traffic, asked only by phones that also ask VPN names', ['okvmm.tech','stspipe.net','assetsconfigcdn.org','firwinds.site']),
    ('Telemetry, ad, storage and backend hosts of free VPN apps, seen in real traffic and asked almost only by phones that also use VPN apps', ['tk0x1.com','envoy-track.core-002-ew4.ov1o.com','app-ads-services.com','ad-host-backup-america.oss-us-west-1.aliyuncs.com','new-sign-xghwyaxeiq-uc.a.run.app']),
    ('What-is-my-IP services that VPN apps use to verify their exit', ['ipify.org','ipinfo.io','ipapi.co','ip-api.com']),
    ('Tor and Orbot helper services the large lists did not carry: bridge distribution through a DNS tunnel, and the registration service of the conjure transport', ['bypasscensorship.org','ruhnama.net','refraction.network']),
   ]),
 'encrypted-dns': ('Encrypted DNS resolvers (DoH and DoT)',
   'Public DNS-over-HTTPS and DNS-over-TLS resolver names that phones and browsers use to get around a local DNS filter.',
   [
    ('Resolvers', ['one.one.one.one','cloudflare-dns.com','1dot1dot1dot1.cloudflare-dns.com','chrome.cloudflare-dns.com','mozilla.cloudflare-dns.com','family.cloudflare-dns.com','security.cloudflare-dns.com','dns.cloudflare.com','dns.google','dns.google.com','dns64.dns.google','doh.dns.apple.com','doh-dns-apple-com.v.aaplimg.com','dns.quad9.net','dns9.quad9.net','dns10.quad9.net','dns11.quad9.net','dns.adguard.com','dns.adguard-dns.com','family.adguard-dns.com','unfiltered.adguard-dns.com','dns.nextdns.io','doh.opendns.com','doh.familyshield.opendns.com','doh.cleanbrowsing.org','dns.sb','doh.pub','dns.alidns.com','dns.controld.com']),
   ]),
 'betting-mexico': ('Betting sites, Mexico',
   'Sports betting and online casino sites aimed at Mexico: the ones under .mx names, and offshore casinos that target Mexican players under numbered mirror names, which the large gambling lists did not carry when we added them.',
   [
    ('Sites', ['caliente.mx','codere.mx','playdoit.mx','betano.mx','bet365.mx','strendus.com.mx','winpot.mx','ganabet.mx','betway.mx','betsson.mx','betcris.mx','rushbet.mx','foliatti.mx']),
    ("Hoy777, an online casino seen in real traffic (2026-10-02), and its numbered mirrors; each name's own page read as the same casino", ['888hoy.com','hoy000.com','000hoy.com','hoy111.com','hoy222.com','hoy333.com','hoy444.com','hoy555.com','hoy666.com','hoy777.com','777hoy.com','hoy777.mx','hoy888.com','hoy999.com','999hoy.com','hoy777.app','hoy777.net','hoy777.vip','hoy777casino.com','hoy777.io','hoy7777.com','444hoy.com','555hoy.com','666hoy.com','mars.bingo','mx-hoy777.com','mxhoy777.com','hoy777-juega-mx.com']),
    ('Sister casinos on the same naming pattern and the same game launcher: MEXBOSS and Hoy7 (Hoy 777 Casino)', ['mexboss.com','mexboss.mx','mexboss.vip','111hoy.com','222hoy.com','333hoy.com','hoy7.com','hoy7.mx','hoy77.com','hoy99.com','88hoy.com','99hoy.com']),
    ("The same naming pattern for other countries' players (Peru, Thailand, Bangladesh, Indonesia)", ['hoy222.net','hoy555.net','hoy666.net','hoy111.net','hoy77.net','hoy88.net']),
    ('Other casinos of the same licence holder (Pistis Trade N.V., Curacao), each read on its own page as a casino aimed at Mexico, with their referral hosts and their app download hosts', ['mexswin04.com','mexwincasino.com','mexbosss.me','mexboss21.com','mex-vip.org','okbono.com','mexok.mx','mxluck.mx','mxfun.mx','bonos777.mx','okgana.mx','okgana.biz','reymxs.biz','mxn777.mx','hoywin.com','hoywin3.com','hoywin11.com','mx7k4.com','mx7k.me','mx711.club','mx711games.com','mx-711.com','rey11.com','reylucky2.com','winmxco04.com','betmxsgames.com','bono777win.com','bcxgcv.icu','bq6yt7.xyz','mktmx.com','livemxapp.com','google-app.mx','wehoprint.com']),
    ("The platforms these casinos run on: Betby's sportsbook hosts and a casino game launcher (urlscan shows only online casinos calling it)", ['invisiblesport.com','a8r.games']),
    ('Other casinos and sportsbooks aimed at Mexico that the smaller gambling lists did not carry on 2026-10-02 (licensed and offshore; each read on its own page)', ['betmaster.mx','jugabet.mx','campobet.mx','pickwin.mx','sportiumbet.mx','gana777.mx','fun88mx.app','p999.com','888novo.com','rbd777.bet','aaaawin.app','mx777casino.com','mx777casino.net','casino777mx.net','casinomx777.com','mxm777mx.com','mx-mx777.com']),
   ]),
 'streaming-tv': ('TV and film streaming',
   'Netflix, ViX and the other TV, film and live-video services reachable from Mexico, the Mediastream platform used by Latin American live TV and radio apps, and the video hosts of the platforms that share their apex with other services (Apple TV+, Prime Video, Mercado Play).',
   [
    ('Netflix (names from v2fly/domain-list-community, data/netflix)', ['netflix.com','netflix.net','netflix.ca','nflxext.com','nflximg.com','nflximg.net','nflxsearch.net','nflxso.net','nflxvideo.net','netflix.com.edgesuite.net']),
    ('Mediastream', ['mdstrm.com']),
    ('ViX and TelevisaUnivision (Akta/Anvato video platform on Google Cloud)', ['vix.com','vix.tv','vixplus.com','lura.live','akta.tech','anvato.com','prende.tv','univision.com','univisionnow.com','tudn.com','tudn.mx','lasestrellas.tv','nmas.com.mx','televisa.com','uvnimg.com']),
    ('TV Azteca', ['tvazteca.com','adn40.mx','aztecajalisco.com','aztecabajio.com','aztecachihuahua.com','aztecapuebla.com','aztecayucatan.com','aztecaveracruz.com','aztecasinaloa.com','aztecaqueretaro.com','aztecaquintanaroo.com','aztecamorelos.com','aztecamichoacan.com','aztecalaguna.com','aztecaguerrero.com','aztecaciudadjuarez.com','aztecachiapas.com','aztecaaguascalientes.com','tvaztecabajacalifornia.com','tvaztecasanluispotosi.com']),
    ('Latin American and global streaming services (Claro video, Canela, Pluto TV, Tubi, Max, Disney+, Prime Video, Paramount+, Crunchyroll, DGO, Runtime, Samsung TV Plus, Plex, Xumo, DAZN, FOX One, ESPN, Mubi, Peacock, Fubo, Mercado Play)', ['clarovideo.com','clarovideo.net','canela.tv','pluto.tv','plutotv.net','plutopreprod.tv','tubitv.com','tubi.io','tubi.video','adrise.tv','max.com','hbomax.com','hbomaxcdn.com','discomax.com','hbogo.com','hbonow.com','hbo.com','maxgo.com','disneyplus.com','disney-plus.net','dssott.com','dssedge.com','bamgrid.com','starplus.com','primevideo.com','amazonvideo.com','aiv-cdn.net','aiv-delivery.net','pv-cdn.net','atv-ps.amazon.com','atv-ext.amazon.com','av-na.amazon.com','paramountplus.com','pplusstatic.com','cbsivideo.com','crunchyroll.com','crunchyrollcdn.com','vrv.co','gccrunchyroll.com','directvgo.com','runtime.tv','samsungtvplus.com','samsung.wurl.tv','internetat.tv','samsungcloud.tv','plex.tv','plex.direct','plexapp.com','plex.bz','xumo.com','xumo.tv','dazn.com','indazn.com','dazndn.com','dazn-api.com','foxone.mx','foxsports.com.mx','espn.com.mx','espncdn.com','mubi.com','peacocktv.com','peacock.com','fubo.tv','play.mercadolibre.com.mx']),
    ('Apple TV+ video hosts only (never the Apple apexes, which carry the App Store, iCloud and updates)', ['tv.apple.com','tv.v.aaplimg.com','hls-svod.itunes.apple.com','hls-svod-ve.itunes.g.aaplimg.com','hls-svod-aoc-ve.itunes.g.aaplimg.com']),
    ('Live streaming and video sharing platforms (Twitch, Kick, Trovo, Nimo TV, Tango, Vimeo, Dailymotion, Rumble, Odysee, Coub)', ['twitch.tv','ext-twitch.tv','ttvnw.net','jtvnw.net','twitchcdn.net','twitchsvc.net','kick.com','trovo.live','nimo.tv','tango.me','vimeo.com','vimeocdn.com','vhx.tv','vimeoondemand.com','livestream.com','dailymotion.com','dmcdn.net','dm-event.net','rumble.com','rmbl.ws','rumble.cloud','odysee.com','odysee.tv','odysee.live','odycdn.com','coub.com']),
    ('Video sources of Mi Video (Xiaomi) and Anime Center from their app packages: MangoTV, the Xiaomi video host (hostname only), animecenter.network, animeflv.net', ['mgtv.com','globalvideo.cdn.pandora.intl.xiaomi.com','animecenter.network','animeflv.net']),
   ]),
 'youtube': ('YouTube',
   'YouTube, its video hosts and its app API. Blocking googlevideo.com also stops YouTube video embedded in other sites.',
   [
    ('YouTube', ['youtube.com','youtu.be','ytimg.com','googlevideo.com','youtubei.googleapis.com']),
    ('YouTube names the NextDNS service definition carries and ours did not', ['youtube-nocookie.com','youtube.googleapis.com','youtubekids.com','yt3.ggpht.com']),
   ]),
 'short-video': ('Short video and short drama apps',
   'Short-video and micro-drama apps beyond TikTok itself (Kwai, SnackVideo, Likee, Bigo Live, Lemon8, the short-drama apps), plus the ByteDance hosts that CapCut and TikTok content load from.',
   [
    ('Clapper', ['myclapper.com']),
    ('CapCut and ByteDance content hosts', ['capcutapi.com','capcut.com','byteoversea.com','byteoversea.net','ibyteimg.com','byteimg.com']),
    ('Short drama apps (ReelShort, DramaBox, ShortMax, GoodShort, FlexTV, NetShort, DramaWave, FreeReels, My Drama, Kalos TV, MoboReels, TopShort, Sereal+, Playlet, Stardust TV, FlickReels, FlareFlow, Melolo, HotMini, BlinkDrama)', ['reelshort.com','crazymaplestudios.com','dramabox.com','dramaboxdb.com','shorttv.live','goodshort.com','goodreels.com','flextv.cc','netshort.com','netshort.net','mydramawave.com','free-reels.com','my-drama.com','kalostv.com','moboreels.com','cdreader.com','topshortapp.com','tikshortsbox.com','sereal.com','serealplus.com','serealshort.com','playlet.com','stardusttv.cc','stardust-tv.com','flickreels.net','farsunpteltd.com','flareflow.tv','melolo.org','hotminidrama.com','blinkdrama.life']),
    ('Kwai and SnackVideo (Kuaishou), with the ad and analytics hosts the app asks beside its own', ['kwai.com','kwai.net','kwai-pro.com','kwaipros.com','yximgs.com','kwimgs.com','kw.ai','snackvideo.com','kuaishou.com','gifshow.com','ksapisrv.com','kslawin.com','kwd.100.app','ap4r.com','adaether.com','mythad.com','dropz-k.com','xxpkg.com']),
    ('Likee, Bigo Live and Hago (JOYY), Lemon8 (ByteDance), rednote', ['likee.video','like.video','likeevideo.com','like-video.com','likeevideo.ru','likeimo.tech','liketech.tech','hzmklvdieo.com','bigo.tv','bigolive.tv','bigovideo.tv','bigo.sg','ihago.net','lemon8-app.com','lemon8cdn.com','xiaohongshu.com','xhscdn.com']),
    ('Short-drama and short-video apps on the Mexico charts of 2026-09-30 (NiceTV, Halo Reels, ReelMax, Drama World, the FreeReels and DramaWave video hosts, Seekee) and KwaiCut, from the apps own sites and public app traffic data (AppGoblin, BeVigil)', ['nicetvs.net','haloreels.net','shortreelmax.com','dramafuture.com','vodplayvideo.net','vodplayvideo.com','vodglcdn.com','buscari.com','seekee.ai','newsparkking.com','kwai-cut.com','kittyfunny.com','inkuai.com']),
   ]),
 'shopping': ('Shopping apps',
   'Temu and its content network.',
   [
    ('Temu', ['temu.com','kwcdn.com']),
   ]),
 'pinterest': ('Pinterest',
   'Pinterest and its image hosts.',
   [
    ('Pinterest', ['pinterest.com','pinimg.com']),
   ]),
 'social': ('Social apps beyond the big four',
   'Threads, Reddit, Tumblr, Bluesky and 9GAG. Facebook, Instagram, TikTok and Snapchat are on the large public social lists and are not repeated here.',
   [
    ('Threads, Reddit, Tumblr, Bluesky, 9GAG', ['threads.com','threads.net','reddit.com','redd.it','redditmedia.com','redditstatic.com','tumblr.com','bsky.app','bsky.social','bsky.network','9gag.com','9cache.com']),
    ('Random video chat and live apps on the Mexico charts (OmeTV, SuperLive), from the apps own sites and public app traffic data', ['ome.tv','ometv.chat','point-of-entry.com','apps-host.com','null-point.com','foto-pin.com','superlivellc.com','apispl2.link','sprlv.link','superlivechat.tv']),
   ]),
 'video-downloaders': ('YouTube clients, video downloaders and third-party YouTube front ends',
   'Apps and sites that play or download YouTube, TikTok, Facebook and Instagram video through their own servers, so they keep working when the platforms themselves are blocked by name: Snaptube and Lark Player (Mobiuspace), Pure Tuber, Vidmate, TubeMate, YMusic, NewPipe, ReVanced, the web downloaders, and the public Invidious and Piped instances.',
   [
    ('Snaptube and Lark Player (Mobiuspace) and their backends', ['snaptube.com','snaptube.app','snaptubead.com','snaptubeapp.com','snapdownloads.com','snaptube.in','ad-snaptube.app','snaptube.mx','falconnet.app','ad-vastvideo.com','larkplayer.com','larkplayerapp.com','larkgame.com','mobiuspace.net','mobiuspace.com']),
    ('Snaptube and Lark Player backend names that share certificates with snaptube.app and larkplayerapp.com (certificate transparency, 2026-09-30)', ['thejeu.com','themsic.com','gdflpr.com','gdfsnt.com']),
    ('Other YouTube clients and video downloader apps (Pure Tuber, Vidmate, TubeMate, YMusic, NewPipe, ReVanced, InsTube, Videoder, UC Browser)', ['puretuber.com','premiumtuberapp.com','vidmateapp.com','vdmapk.com','vidssave.com','facebdownloader.com','fasttik.com','igvideodownloader.net','vidmate.net','tubemate.net','ymusic.io','newpipe.net','revanced.app','vanced.app','instube.com','videoder.com','videoder.net','ucweb.com','ucshare.app']),
    ('Web downloaders (TikTok, YouTube, Tubidy)', ['snaptik.app','ssstik.io','ssstik.link','ssstwitter.com','reelsvideo.io','tikmate.online','y2mate.com','y2mate.is','yt1s.com','savefrom.net','sfrom.net','tubidy.ws','tubidy.llc','tubidy.cool','tubidy.mobi','tubidy.com','tubidy.buzz','tubidy.cv']),
    ('Invidious and Piped instances (third-party YouTube front ends that proxy the video through their own hosts; instance lists read 2026-09-30)', ['invidious.io','nadeko.net','nerdvpn.de','f5.si','chocolatemoo53.com','tiekoetter.com','piped.video','kavin.rocks','leptons.xyz','nosebs.ru','privacy.com.de','adminforge.de','piped.yt','drgns.space','ggtyler.dev','owo.si','ducks.party','codespace.cz','reallyaweso.me','private.coffee','darkness.services','orangenet.cc','libretube.dev']),
    ('YouTube front ends on the Mexico charts (DailyTube, GreenTuber) and the PeerTube hosts GreenTuber falls back to', ['aimxhub.com','dewrain.life','akisinn.info','vaicore.store','dailytube.pro','yougreentube.com','utuber.top','greentuapp.com','yougreentube.ru','greentuber.net','framatube.org','sepiasearch.org']),
   ]),
 'games-mobile': ('Mobile game publishers',
   'The publishers and titles behind the games most installed on Android and iPhone in Mexico: Roblox, Free Fire (Garena), PUBG Mobile, Call of Duty Mobile, Supercell, Mobile Legends (Moonton), Fortnite (Epic), Genshin Impact (HoYoverse), Candy Crush (King), Pokemon GO (Niantic, now Scopely), 8 Ball Pool (Miniclip), Subway Surfers (SYBO), Among Us, eFootball (Konami), EA SPORTS FC, Playrix, Zynga, Voodoo, Kwalee and Lion Studios. Whole publisher domains, so their account, support and store pages go too. Ad networks the games share with other apps (AppLovin, Unity Ads, ironSource) are deliberately not here.',
   [
    ('Roblox', ['roblox.com','rbxcdn.com','rbxtrk.com','rbxinfra.net','roblox.net','roblox.us','roblox.co.uk']),
    ('Garena and Free Fire', ['garena.com','freefiremobile.com','ffesports.com','garena.sg']),
    ('PUBG Mobile (Tencent, Level Infinite)', ['pubgmobile.com','gpubgm.com','amsoveasea.com']),
    ('Call of Duty Mobile (Activision)', ['callofduty.com','activision.com']),
    ('Supercell', ['supercell.com','supercell.net','clashofclans.com','mo.co']),
    ('Moonton (Mobile Legends)', ['moonton.com','viztagame.com']),
    ('Epic Games (Fortnite)', ['epicgames.com','unrealengine.com','fortnite.com']),
    ('HoYoverse', ['hoyoverse.com','mihoyo.com']),
    ('King (Candy Crush)', ['king.com','candycrushsaga.com','midasplayer.net','midasplayer.cloud']),
    ('Niantic and Scopely (Pokemon GO, Monopoly GO, Stumble Guys)', ['nianticlabs.com','nianticstatic.com','pokemongo.com','scopely.com','withbuddies.com']),
    ('Miniclip (8 Ball Pool, Agar.io)', ['miniclip.com','8ballpool.com','agar.io','miniclippt.com']),
    ('SYBO (Subway Surfers)', ['sybogames.com','subwaysurfers.com','subwaysurferscity.com']),
    ('Innersloth (Among Us)', ['innersloth.com','among.us']),
    ('Konami (eFootball)', ['konami.net','konami.com']),
    ('Electronic Arts (EA SPORTS FC Mobile)', ['ea.com','easports.com','eamobile.com','tnt-ea.com']),
    ('Playrix, Zynga, Voodoo, Kwalee, Lion Studios', ['playrix.com','zynga.com','zyngagames.com','voodoo.io','kwalee.com','lionstudios.cc']),
    ('Game backends seen in real traffic (Tencent Level Infinite for PUBG Mobile; a casual-game publisher)', ['listdl.com','dailyinnovation.biz']),
   ]),
 'piracy-streaming': ('Pirate film and series streaming',
   'Free pirate film and series sites in Spanish and Latin American Spanish, their brand and sister domains, and the video file hosts their players stream from. The sites were seen in real traffic or read on their own pages; the video-host names come from the ResolveURL project. Only names the large anti-piracy lists did not carry when we added them. Use it beside HaGeZi Anti-Piracy, not instead of it.',
   [
    ("PeliSmart (smartpelis.tv): its own domains and redirects, MagisTV 24 (same WordPress pages with the same creation times, same Cloudflare nameservers), and the anime sister its pages link to", ["smartpelis.tv", "smartpeli.tv", "smartpeli.com", "smartpeli.app", "pelismart.tv", "magistv24.com", "flvanime.org"]),
    ("Other sites under the PeliSmart name (read on their own pages)", ["pelismart.top", "pelismart.lol", "pelismart.mov"]),
    ("Other Spanish-language pirate film sites and embed APIs (read on their own pages, or named as sources by the WebStreamr project)", ["cuevana3.is", "homecine.to", "cinehdplus.gratis", "verhdlink.cam", "playlatinsrc.co"]),
    ("Video hosts the players stream from: Fastream (every player on a PeliSmart film page is a fastream embed, served from sNN.fastream.to)", ["fastream.to"]),
    ("Video host family Streamwish (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["streamwish.com", "ajmidyad.sbs", "khadhnayad.sbs", "yadmalik.sbs", "hayaatieadhab.sbs", "kharabnahs.sbs", "atabkhha.sbs", "atabknha.sbs", "atabknhk.sbs", "atabknhs.sbs", "abkrzkr.sbs", "abkrzkz.sbs", "wishembed.pro", "mwish.pro", "strmwis.xyz", "awish.pro", "dwish.pro", "vidmoviesb.xyz", "embedwish.com", "cilootv.store", "uqloads.xyz", "tuktukcinema.store", "doodporn.xyz", "ankrzkz.sbs", "volvovideo.top", "streamwish.site", "wishfast.top", "ankrznm.sbs", "sfastwish.com", "eghjrutf.sbs", "eghzrutw.sbs", "guxhag.com", "playembed.online", "egsyxurh.sbs", "egtpgrvh.sbs", "flaswish.com", "obeywish.com", "cdnwish.com", "javsw.me", "cinemathek.online", "trgsfjll.sbs", "fsdcmo.sbs", "hailindihg.com", "anime4low.sbs", "mohahhda.site", "ma2d.store", "dancima.shop", "swhoi.com", "aiavh.com", "gsfqzmqu.sbs", "jodwish.com", "swdyu.com", "strwish.com", "asnwish.com", "kravaxxa.com", "wishonly.site", "playerwish.com", "katomen.store", "hlswish.com", "streamwish.fun", "swishsrv.com", "iplayerhls.com", "hlsflast.com", "4yftwvrdz7.sbs", "ghbrisk.com", "hgbazooka.com", "eb8gfmjn71.sbs", "cybervynx.com", "edbrdl7pab.sbs", "stbhg.click", "dhcplay.com", "strwish.xyz", "gradehgplus.com", "tryzendm.com", "hglink.to", "dumbalag.com", "haxloppd.com", "davioad.com", "uasopt.com", "hgcloud.to"]),
    ("Video host family FileLions and VidHide (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["filelions.com", "filelions.to", "ajmidyadfihayh.sbs", "alhayabambi.sbs", "vidhideplus.com", "moflix-stream.click", "azipcdn.com", "mlions.pro", "alions.pro", "dlions.pro", "filelions.live", "motvy55.store", "filelions.xyz", "lumiawatch.top", "filelions.online", "javplaya.com", "fviplions.com", "egsyxutd.sbs", "filelions.site", "filelions.co", "vidhide.com", "vidhidepro.com", "vidhidevip.com", "javlion.xyz", "fdewsdc.sbs", "anime7u.com", "coolciima.online", "gsfomqu.sbs", "vidhidepre.com", "katomen.online", "vidhide.fun", "vidhidehub.com", "dhtpre.com", "6sfkrspw4u.sbs", "streamvid.su", "movearnpre.com", "bingezove.com", "dingtezuni.com", "dinisglows.com", "ryderjet.com", "e4xb5c2xnz.sbs", "smoothpre.com", "videoland.sbs", "taylorplayer.com", "mivalyo.com", "vidhidefast.com", "peytonepre.com", "dintezuvio.com", "callistanise.com", "minochinos.com", "earnvids.xyz", "morencius.com"]),
    ("Video host family FileMoon (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["filemoon.org"]),
    ("Video host family VOE and its rotating redirect names (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["voe-unblock.com", "voe-unblock.net", "voeunblock.com", "un-block-voe.net", "voeunbl0ck.com", "voeunblck.com", "voe-un-block.com", "jonathansociallike.com", "voeun-block.net", "v-o-e-unblock.com", "edwardarriveoften.com", "nathanfromsubject.com", "audaciousdefaulthouse.com", "launchreliantcleaverriver.com", "kennethofficialitem.com", "reputationsheriffkennethsand.com", "fittingcentermondaysunday.com", "lukecomparetwo.com", "housecardsummerbutton.com", "fraudclatterflyingcar.com", "wolfdyslectic.com", "bigclatterhomesguideservice.com", "uptodatefinishconferenceroom.com", "jayservicestuff.com", "realfinanceblogcenter.com", "tinycat-voe-fashion.com", "35volitantplimsoles5.com", "20demidistance9elongations.com", "telyn610zoanthropy.com", "toxitabellaeatrebates306.com", "greaseball6eventual20.com", "745mingiestblissfully.com", "19turanosephantasia.com", "30sensualizeexpression.com", "321naturelikefurfuroid.com", "449unceremoniousnasoseptal.com", "guidon40hyporadius9.com", "cyamidpulverulence530.com", "boonlessbestselling244.com", "antecoxalbobbing1010.com", "matriculant401merited.com", "scatch176duplicities.com", "availedsmallest.com", "counterclockwisejacky.com", "simpulumlamerop.com", "paulkitchendark.com", "metagnathtuggers.com", "gamoneinterrupted.com", "chromotypic.com", "crownmakermacaronicism.com", "generatesnitrosate.com", "yodelswartlike.com", "figeterpiazine.com", "strawberriesporail.com", "valeronevijao.com", "timberwoodanotia.com", "apinchcaseation.com", "nectareousoverelate.com", "nonesnanking.com", "kathleenmemberhistory.com", "stevenimaginelittle.com", "jamiesamewalk.com", "bradleyviewdoctor.com", "sandrataxeight.com", "graceaddresscommunity.com", "shannonpersonalcost.com", "cindyeyefinal.com", "michaelapplysome.com", "sethniceletter.com", "brucevotewithin.com", "rebeccaneverbase.com", "loriwithinfamily.com", "roberteachfinal.com", "erikcoldperson.com", "jasminetesttry.com", "heatherdiscussionwhen.com", "robertplacespace.com", "alleneconomicmatter.com", "josephseveralconcern.com", "donaldlineelse.com", "lisatrialidea.com", "toddpartneranimal.com", "jamessoundcost.com", "brittneystandardwestern.com", "sandratableother.com", "robertordercharacter.com", "maxfinishseveral.com", "chuckle-tube.com", "kristiesoundsimply.com", "adrianmissionminute.com", "richardsignfish.com", "jennifercertaindevelopment.com", "diananatureforeign.com", "goofy-banana.com", "mariatheserepublican.com", "johnalwayssame.com", "kellywhatcould.com", "jilliandescribecompany.com", "mikaylaarealike.com", "christopheruntilpoint.com", "walterprettytheir.com", "crystaltreatmenteast.com", "lauradaydo.com", "lancewhosedifficult.com", "dianaavoidthey.com", "jefferycontrolmodel.com", "marissasharecareer.com", "charlestoughrace.com", "ianrequireadult.com", "timmaybealready.com", "jessicayeahcatch.com", "johnbeyondnation.com", "jeanprofessorcentral.com", "juliewomanwish.com", "garylargeavailable.com", "jennifereconomicgive.com", "pamelachangemission.com", "ellenpoliticalfollow.com", "caseyimpactstation.com", "matthewhotelscience.com", "jessicachoosemake.com", "stevenfamilyedge.com", "tracylocalschool.com", "eugenemakedraw.com", "johnfullwonder.com", "katherineschoolphone.com", "jamesbornmain.com", "jeremyparticipantanything.com"]),
    ("Video host family DoodStream (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["dood.cx", "ds2video.com", "d0o0d.com", "d000d.com", "dood.work", "all3do.com", "doply.net", "vvide0.com", "playmogo.com"]),
    ("Video host family Streamtape (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["strtape.cloud", "streamtape.net", "streamta.pe", "streamtape.site", "strcloud.link", "strcloud.club", "strtpe.link", "streamtape.cc", "scloud.online", "stape.fun", "streamadblockplus.com", "shavetape.cash", "streamtape.to", "streamta.site", "streamadblocker.xyz", "tapewithadblock.org", "adblocktape.wiki", "antiadtape.com", "streamtape.xyz", "tapeblocker.com", "streamnoads.com", "tapeadvertisement.com", "tapeadsenjoyer.com", "tpead.net", "strtape.site", "strtapeadblock.me", "gettapeads.com", "streamtapeadblock.art", "streamtapeadblockuser.xyz", "advtpe.com"]),
    ("Video host family Mixdrop (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["mixdrop.to", "mixdrop.sx", "mixdrop.bz", "mixdrop.ch", "mixdrp.co", "mixdrp.to", "mixdrop.gl", "mixdrop.club", "mixdroop.bz", "mixdroop.co", "mixdrop.vc", "mdy48tn97.com", "md3b0j6hj.com", "mdbekjwqa.pw", "mdfx9dc8n.net", "mixdropjmk.pw", "mixdrop21.net", "mixdrop.is", "mixdrop.si", "mixdrop23.net", "mixdrop.nu", "mixdrop.ms", "mdzsmutpcvykb.net", "mixdrop.ps", "mxdrop.to", "mixdrop.sb", "mixdrop.my", "m1xdrop.com", "m1xdrop.click", "mxdrop.sx", "mixdrp.click", "miixdrop.net", "miiixdrop.net", "miiiixdrop.net"]),
    ("Video host family Uqload (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["uqload.com", "uqload.co", "uqload.io", "uqload.to", "uqload.ws", "uqload.net", "uqload.cx", "uqload.bz", "uqload.org", "uqload.is", "uqload.vc"]),
    ("Video host family Upstream (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["upstream.to"]),
    ("Video host family LuluStream (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["luluvdo.com", "732eg54de642sa.sbs", "streamhihi.com", "luluvdoo.com", "d00ds.site"]),
    ("Video host family GoodStream (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["goodstream.uno", "goodstream.one"]),
    ("Video host family Vidmoly (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["vidmoly.to", "vidmoly.org"]),
    ("Video host family Netu, HQQ and Waaw (domains from the ResolveURL project's plugin file, read 2026-10-01; names already on HaGeZi Anti-Piracy or NextDNS streaming-video left out)", ["waaw.ac", "netu.ac", "hqq.ac", "waaw.tv", "waaw.to", "netu.to", "hqq.to", "doplay.store", "stbnetu.xyz", "brightmindwave.com", "ncdn22.xyz", "oyohd.one", "player.sorozatok.me", "vidmoly.cam", "0gomovies.beer"]),
   ]),
 'ads': ('Ad networks the large ad lists miss',
   'Ad and pop-under network names seen in real traffic that HaGeZi Multi PRO did not carry when we added them. A gap-filler: use it beside a large ad list, not instead of one.',
   [
    ('Pop-under network loaded on every page of a pirate film site (PeliSmart); its home pages redirect to google.com and its sister names share the same servers', ['refusedconsulting.com','articleexchangedquell.com','magnificentbearing.com']),
   ]),
 'app-bloat': ('Carrier preload, ad SDKs and app bloat',
   'Names that phones ask because of the software the carrier or the phone maker put on them, or because of the ad and mediation SDKs inside free apps: nothing a person opened on purpose. Identified in real traffic by registry, certificate and app-traffic records. Ad networks are not here as a category; the large public ad lists do that job, and the gaps we find in them go on the ads list.',
   [
    ('Carrier and OEM app preload and on-device ads (ironSource Aura, AppLovin Array, Siprocal, the Digital Turbine installer under a Telcel name, DialMyApp)', ['isappcloud.com','al-array.com','arrayengine.com','siprocal.com','siprocalads.com','appamx.com','dialmyapp.com']),
    ('Ad mediation and exchange SDKs inside free apps (TopOn, BidMachine, Airfind)', ['mosspf.net','mosspf.com','mossru.com','bktpcross.com','toponad.com','blueduckredapple.com','airfind.com']),
    ('Ad tags and abandoned callback names phones still ask', ['qzwxrtyk.com','ertyuioq.com','app-null.com']),
   ]),
}
os.makedirs(ROOT + '/lists', exist_ok=True)
counts = {}
for key, (title, desc, groups) in LISTS.items():
    seen = set(); out = []
    n = sum(len(g[1]) for g in groups)
    out += ['! Title: NSY DNS Blocklist: ' + title,
            '! Description: ' + desc,
            '! Homepage: ' + HOME,
            '! Last modified: ' + TODAY,
            '! Entries: ' + str(n),
            '! Syntax: Adblock style. ||example.com^ blocks the domain and all of its subdomains.',
            '!']
    for gname, doms in groups:
        out.append('! ' + gname)
        for d in doms:
            assert d not in seen and d == d.lower().strip(), d
            seen.add(d); out.append('||' + d + '^')
        out.append('!')
    open(ROOT + '/lists/' + key + '.txt', 'w', encoding='utf-8', newline='\n').write('\n'.join(out).rstrip('!\n') + '\n')
    counts[key] = n
print(counts, sum(counts.values()))
