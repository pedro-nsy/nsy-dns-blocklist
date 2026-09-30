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
    ('Small mobile VPN apps and their backends, seen in real traffic', ['luxvpn.cc','vpnlux.cc','vpnrapid.net','thundervpn.net','thundervpnwin.com','free-signal.com','melonvpn.com','suinfra.com','ourip.info','mobilejump.mobi','gofastvpn.com','starwayvpn.xyz','astravpn.xyz','funsol.cloud','bolt-backup.matee-b04.workers.dev','vpnpremiums.com','us-central1-vpn-platform-prod.cloudfunctions.net','tumogle.tech','bytegle.tech','news-cdn.site','apgdmsiifk.com','rateyourispprovider.com','signallab.org','keysuccess.site','securestartup.business','prebreeze.club','cyberanalytics.link','graphlist.dev','zigzagwand.art']),
    ('Sister apps of the families above, from their store pages and public app traffic data (AppGoblin)', ['matrixmobile.net','freevpnapp.net','vpnmelon.com','securesignal.app','alarmpushes.com','fastv.mobi']),
    ("Proton VPN (from Proton's own app source on GitHub: alternative-routing bootstrap, download host, server names)", ['protonpro.xyz','protondownload.com','protonvpn.net']),
    ('VPN app families behind the small apps (publisher sites, the FOCI 2025 paper, app store pages)', ['inconnecting.com','turbovpn.com','secureguardpro.com','materialsofpro.com','snapillustrates.com','autumnbreeze.co','signalsecurevpn.com','xvpn.io','potatovpn.io','freeconnectedlimited.com','vpnsuper.com','unlimitedvpn.im','hvnstore.com','surfsharkstatus.com','uymgg1.com','sir90hl.com','s0r4nd0m.com','hsselite.com','northghost.com','aura-servers.com','cloudflare-gateway.com','cloudflareportal.com','cloudflareok.com','cloudflarecp.com','zerotier.com','psiphon-conduit.com','bright-sdk.com','h-cdn.com','holax.io','opera-proxy.net','alohabrowser.com','alohaprofile.com']),
    ('VPN app backends seen in real traffic, asked only by phones that also ask VPN names', ['okvmm.tech','stspipe.net','assetsconfigcdn.org']),
    ('What-is-my-IP services that VPN apps use to verify their exit', ['ipify.org','ipinfo.io','ipapi.co','ip-api.com']),
   ]),
 'encrypted-dns': ('Encrypted DNS resolvers (DoH and DoT)',
   'Public DNS-over-HTTPS and DNS-over-TLS resolver names that phones and browsers use to get around a local DNS filter.',
   [
    ('Resolvers', ['one.one.one.one','cloudflare-dns.com','1dot1dot1dot1.cloudflare-dns.com','chrome.cloudflare-dns.com','mozilla.cloudflare-dns.com','family.cloudflare-dns.com','security.cloudflare-dns.com','dns.cloudflare.com','dns.google','dns.google.com','dns64.dns.google','doh.dns.apple.com','doh-dns-apple-com.v.aaplimg.com','dns.quad9.net','dns9.quad9.net','dns10.quad9.net','dns11.quad9.net','dns.adguard.com','dns.adguard-dns.com','family.adguard-dns.com','unfiltered.adguard-dns.com','dns.nextdns.io','doh.opendns.com','doh.familyshield.opendns.com','doh.cleanbrowsing.org','dns.sb','doh.pub','dns.alidns.com','dns.controld.com']),
   ]),
 'betting-mexico': ('Betting sites, Mexico',
   'Sports betting and casino sites that operate under .mx names, some of which the large gambling lists did not carry when we added them.',
   [
    ('Sites', ['caliente.mx','codere.mx','playdoit.mx','betano.mx','bet365.mx','strendus.com.mx','winpot.mx','ganabet.mx','betway.mx','betsson.mx','betcris.mx','rushbet.mx','foliatti.mx']),
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
    ('Kwai and SnackVideo (Kuaishou), with the ad and analytics hosts the app asks beside its own', ['kwai.com','kwai.net','kwai-pro.com','kwaipros.com','yximgs.com','kwimgs.com','kw.ai','snackvideo.com','kuaishou.com','gifshow.com','ksapisrv.com','ap4r.com','adaether.com','mythad.com','dropz-k.com']),
    ('Likee, Bigo Live and Hago (JOYY), Lemon8 (ByteDance), rednote', ['likee.video','like.video','likeevideo.com','like-video.com','likeevideo.ru','likeimo.tech','liketech.tech','hzmklvdieo.com','bigo.tv','bigolive.tv','bigovideo.tv','bigo.sg','ihago.net','lemon8-app.com','lemon8cdn.com','xiaohongshu.com','xhscdn.com']),
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
   ]),
 'video-downloaders': ('YouTube clients, video downloaders and third-party YouTube front ends',
   'Apps and sites that play or download YouTube, TikTok, Facebook and Instagram video through their own servers, so they keep working when the platforms themselves are blocked by name: Snaptube and Lark Player (Mobiuspace), Pure Tuber, Vidmate, TubeMate, YMusic, NewPipe, ReVanced, the web downloaders, and the public Invidious and Piped instances.',
   [
    ('Snaptube and Lark Player (Mobiuspace) and their backends', ['snaptube.com','snaptube.app','snaptubead.com','snaptubeapp.com','snapdownloads.com','snaptube.in','ad-snaptube.app','snaptube.mx','falconnet.app','ad-vastvideo.com','larkplayer.com','larkplayerapp.com','larkgame.com','mobiuspace.net','mobiuspace.com']),
    ('Other YouTube clients and video downloader apps (Pure Tuber, Vidmate, TubeMate, YMusic, NewPipe, ReVanced, InsTube, Videoder, UC Browser)', ['puretuber.com','premiumtuberapp.com','vidmateapp.com','vdmapk.com','vidssave.com','facebdownloader.com','fasttik.com','igvideodownloader.net','vidmate.net','tubemate.net','ymusic.io','newpipe.net','revanced.app','vanced.app','instube.com','videoder.com','videoder.net','ucweb.com','ucshare.app']),
    ('Web downloaders (TikTok, YouTube, Tubidy)', ['snaptik.app','ssstik.io','ssstik.link','ssstwitter.com','reelsvideo.io','tikmate.online','y2mate.com','y2mate.is','yt1s.com','savefrom.net','sfrom.net','tubidy.ws','tubidy.llc','tubidy.cool','tubidy.mobi','tubidy.com','tubidy.buzz','tubidy.cv']),
    ('Invidious and Piped instances (third-party YouTube front ends that proxy the video through their own hosts; instance lists read 2026-09-30)', ['invidious.io','nadeko.net','nerdvpn.de','f5.si','chocolatemoo53.com','tiekoetter.com','piped.video','kavin.rocks','leptons.xyz','nosebs.ru','privacy.com.de','adminforge.de','piped.yt','drgns.space','ggtyler.dev','owo.si','ducks.party','codespace.cz','reallyaweso.me','private.coffee','darkness.services','orangenet.cc','libretube.dev']),
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
