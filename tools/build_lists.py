# Builds the files under lists/ from the entries below.
# Usage: python tools/build_lists.py YYYY-MM-DD
import os, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = sys.argv[1]
HOME = 'https://github.com/pedro-nsy/nsy-dns-blocklist'
LISTS = {
 'vpn-proxy': ('VPN and proxy apps',
   'Domains of VPN, proxy and anonymizer apps and services: the well-known brands, and small mobile VPN apps we found in real traffic that the big public lists did not carry when we found them.',
   [('Well-known services', ['protonvpn.com','protonvpn.ch','vpn-api.proton.me','surfshark.com','tunnelbear.com','superunlimited.com','mullvad.net','sec-tunnel.com','nordvpn.com','nordcdn.com','expressvpn.com','windscribe.com','hotspotshield.com','anchorfree.com','cyberghostvpn.com','privateinternetaccess.com','hide.me','hidemyass.com','zenmate.com','betternet.co','psiphon.ca','psiphon3.com','cloudflareclient.com','getoutline.org','ivpn.net','purevpn.com','vyprvpn.com','torguard.net','atlasvpn.com','ultrasurf.us','lantern.io','getlantern.org','torproject.org','x-vpn.com','turbovpn.co','vpnproxymaster.com','hola.org','holavpn.net','urban-vpn.com','browsec.com','speedify.com']),
    ('Small mobile VPN apps and their backends, seen in real traffic', ['luxvpn.cc','vpnlux.cc','vpnrapid.net','thundervpn.net','thundervpnwin.com','free-signal.com','melonvpn.com','suinfra.com','ourip.info','mobilejump.mobi','gofastvpn.com','starwayvpn.xyz','astravpn.xyz','funsol.cloud','bolt-backup.matee-b04.workers.dev','vpnpremiums.com','us-central1-vpn-platform-prod.cloudfunctions.net','tumogle.tech','bytegle.tech','news-cdn.site','apgdmsiifk.com','rateyourispprovider.com','signallab.org','keysuccess.site','securestartup.business','prebreeze.club','cyberanalytics.link','graphlist.dev','zigzagwand.art']),
    ('Sister apps of the families above, from their store pages and public app traffic data (AppGoblin)', ['matrixmobile.net','freevpnapp.net','vpnmelon.com','securesignal.app','alarmpushes.com','fastv.mobi'])]),
 'encrypted-dns': ('Encrypted DNS resolvers (DoH and DoT)',
   'Public DNS-over-HTTPS and DNS-over-TLS resolver names that phones and browsers use to get around a local DNS filter.',
   [('Resolvers', ['one.one.one.one','cloudflare-dns.com','1dot1dot1dot1.cloudflare-dns.com','chrome.cloudflare-dns.com','mozilla.cloudflare-dns.com','family.cloudflare-dns.com','security.cloudflare-dns.com','dns.cloudflare.com','dns.google','dns.google.com','dns64.dns.google','doh.dns.apple.com','doh-dns-apple-com.v.aaplimg.com','dns.quad9.net','dns9.quad9.net','dns10.quad9.net','dns11.quad9.net','dns.adguard.com','dns.adguard-dns.com','family.adguard-dns.com','unfiltered.adguard-dns.com','dns.nextdns.io','doh.opendns.com','doh.familyshield.opendns.com','doh.cleanbrowsing.org','dns.sb','doh.pub','dns.alidns.com','dns.controld.com'])]),
 'betting-mexico': ('Betting sites, Mexico',
   'Sports betting and casino sites that operate under .mx names, some of which the large gambling lists did not carry when we added them.',
   [('Sites', ['caliente.mx','codere.mx','playdoit.mx','betano.mx','bet365.mx','strendus.com.mx','winpot.mx','ganabet.mx','betway.mx','betsson.mx','betcris.mx','rushbet.mx','foliatti.mx'])]),
 'streaming-tv': ('TV and film streaming',
   'Netflix and the Mediastream platform used by Latin American live TV and radio apps.',
   [('Netflix (names from v2fly/domain-list-community, data/netflix)', ['netflix.com','netflix.net','netflix.ca','nflxext.com','nflximg.com','nflximg.net','nflxsearch.net','nflxso.net','nflxvideo.net','netflix.com.edgesuite.net']),
    ('Mediastream', ['mdstrm.com'])]),
 'youtube': ('YouTube',
   'YouTube, its video hosts and its app API. Blocking googlevideo.com also stops YouTube video embedded in other sites.',
   [('YouTube', ['youtube.com','youtu.be','ytimg.com','googlevideo.com','youtubei.googleapis.com'])]),
 'short-video': ('Short video and short drama apps',
   'Short-video and micro-drama apps beyond TikTok itself, plus the ByteDance hosts that CapCut and TikTok content load from.',
   [('Clapper', ['myclapper.com']),
    ('CapCut and ByteDance content hosts', ['capcutapi.com','capcut.com','byteoversea.com','byteoversea.net','ibyteimg.com','byteimg.com']),
    ('Short drama apps (ReelShort, DramaBox, ShortMax, GoodShort, FlexTV, NetShort, DramaWave, FreeReels, My Drama, Kalos TV, MoboReels, TopShort, Sereal+, Playlet, Stardust TV, FlickReels, FlareFlow, Melolo, HotMini, BlinkDrama)', ['reelshort.com','crazymaplestudios.com','dramabox.com','dramaboxdb.com','shorttv.live','goodshort.com','goodreels.com','flextv.cc','netshort.com','netshort.net','mydramawave.com','free-reels.com','my-drama.com','kalostv.com','moboreels.com','cdreader.com','topshortapp.com','tikshortsbox.com','sereal.com','serealplus.com','serealshort.com','playlet.com','stardusttv.cc','stardust-tv.com','flickreels.net','farsunpteltd.com','flareflow.tv','melolo.org','hotminidrama.com','blinkdrama.life'])]),
 'shopping': ('Shopping apps',
   'Temu and its content network.',
   [('Temu', ['temu.com','kwcdn.com'])]),
 'pinterest': ('Pinterest',
   'Pinterest and its image hosts.',
   [('Pinterest', ['pinterest.com','pinimg.com'])]),
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
