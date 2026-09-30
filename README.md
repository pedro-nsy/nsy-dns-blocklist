# NSY DNS Blocklist

Small, focused DNS blocklists for workplace and family networks, organized by what you want to block.

Subscribe only to the lists that match your goal. Each list does one job.

## Why this exists

These lists grew out of day-to-day network administration work. On some networks the internet is there for work, and the people who own them ask for a simple thing: no social video, no betting, and no VPN apps to get around the rules.

The big public blocklists do most of that job, and we use them every day. But when we read real traffic we kept finding gaps:

- small VPN apps that were not on the public lists when we found them
- betting sites that only exist under a local country name
- newer video apps that the large social lists had not picked up yet

Every name in these lists is 1 of 3 things: a service's own published domain, a name we saw in real traffic on a network we manage, or a name taken from a public list that we credit below. When we find a gap, we add it here.

## The lists

| List | What it blocks | Subscribe |
|---|---|---|
| **VPN and proxy apps** | VPN, proxy and anonymizer apps: the well-known brands, small mobile VPN apps we found in real traffic, the publisher families behind them, and the IP-check services the apps use | [`lists/vpn-proxy.txt`](https://raw.githubusercontent.com/pedro-nsy/nsy-dns-blocklist/main/lists/vpn-proxy.txt) |
| **Encrypted DNS resolvers** | Public DoH and DoT resolvers that phones and browsers use to get around a local DNS filter | [`lists/encrypted-dns.txt`](https://raw.githubusercontent.com/pedro-nsy/nsy-dns-blocklist/main/lists/encrypted-dns.txt) |
| **Betting sites, Mexico** | Sports betting and casino sites under .mx names | [`lists/betting-mexico.txt`](https://raw.githubusercontent.com/pedro-nsy/nsy-dns-blocklist/main/lists/betting-mexico.txt) |
| **TV and film streaming** | Netflix, ViX, TV Azteca, Claro video and the other TV, film and live-video services reachable from Mexico, plus the Mediastream platform used by Latin American live TV and radio apps | [`lists/streaming-tv.txt`](https://raw.githubusercontent.com/pedro-nsy/nsy-dns-blocklist/main/lists/streaming-tv.txt) |
| **YouTube** | YouTube, its video hosts and its app API | [`lists/youtube.txt`](https://raw.githubusercontent.com/pedro-nsy/nsy-dns-blocklist/main/lists/youtube.txt) |
| **Short video and short drama apps** | Kwai, SnackVideo, Likee, Bigo Live, Lemon8, Clapper, CapCut, the ByteDance content hosts, and micro-drama apps | [`lists/short-video.txt`](https://raw.githubusercontent.com/pedro-nsy/nsy-dns-blocklist/main/lists/short-video.txt) |
| **Shopping apps** | Temu and its content network | [`lists/shopping.txt`](https://raw.githubusercontent.com/pedro-nsy/nsy-dns-blocklist/main/lists/shopping.txt) |
| **Pinterest** | Pinterest and its image hosts | [`lists/pinterest.txt`](https://raw.githubusercontent.com/pedro-nsy/nsy-dns-blocklist/main/lists/pinterest.txt) |
| **Social apps beyond the big four** | Threads, Reddit, Tumblr, Bluesky and 9GAG (Facebook, Instagram, TikTok and Snapchat are on the large social lists) | [`lists/social.txt`](https://raw.githubusercontent.com/pedro-nsy/nsy-dns-blocklist/main/lists/social.txt) |
| **Mobile game publishers** | Roblox, Free Fire, PUBG Mobile, Call of Duty Mobile, Supercell, Mobile Legends, Fortnite, Genshin, Candy Crush, Pokemon GO, 8 Ball Pool, Subway Surfers, Among Us, eFootball, EA SPORTS FC and the studios behind them | [`lists/games-mobile.txt`](https://raw.githubusercontent.com/pedro-nsy/nsy-dns-blocklist/main/lists/games-mobile.txt) |
| **Carrier preload, ad SDKs and app bloat** | The carriers' and phone makers' app-preload machinery, the ad mediation SDKs inside free apps, and abandoned names phones still call | [`lists/app-bloat.txt`](https://raw.githubusercontent.com/pedro-nsy/nsy-dns-blocklist/main/lists/app-bloat.txt) |
| **YouTube clients and video downloaders** | Snaptube, Lark Player, Pure Tuber, Vidmate, TubeMate, the web downloaders, and the public Invidious and Piped instances that keep YouTube playing when YouTube itself is blocked | [`lists/video-downloaders.txt`](https://raw.githubusercontent.com/pedro-nsy/nsy-dns-blocklist/main/lists/video-downloaders.txt) |

## How to use them

Copy the link of the list you want and add it as a blocklist in your DNS filter.

- **Pi-hole (version 6):** Lists, paste the link, Add blocklist, then update gravity.
- **AdGuard Home:** Filters, DNS blocklists, Add blocklist, Add a custom list.
- **Anything else that reads Adblock style lists** works the same way.

The lists use the Adblock style: `||example.com^` blocks the domain and all of its subdomains.

## What these lists are, and what they are not

- **They fill gaps.** They are meant to sit beside the large lists, not replace them. We use them together with [HaGeZi's DNS blocklists](https://github.com/hagezi/dns-blocklists).
- **They are small and hand-maintained.** Each entry is a whole domain that belongs to the thing being blocked. No shared clouds, no content networks that other apps depend on. They are updated when we find new names.
- **They will block things you may want.** Read a list before you subscribe to it.
- **A DNS list alone does not stop a VPN.** Many VPN apps connect straight to an address and never ask DNS. Blocking the app's own names stops it from signing in and fetching its server list. A firewall has to do the rest.
- **The YouTube list is strict.** It also stops YouTube videos embedded in other sites.

## Found a mistake, or a gap?

Open an issue. Tell us the domain, what it belongs to, and where you saw it. If something here blocks a thing it should not, we want to know.

## Credits

Netflix names come from [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community).

Some VPN app backend names come from the public app traffic data at [AppGoblin](https://appgoblin.info).

Several streaming, social and video-platform names were checked against the per-service definitions of [NextDNS](https://github.com/nextdns/services) and [AdGuard](https://github.com/AdguardTeam/HostlistsRegistry), and the VPN app families against the FOCI 2025 paper "Hidden Links" and the publishers' own pages. The Invidious and Piped instance names come from the projects' own public instance lists.

Maintained by Neufeld Systems.

## Licence

[MIT](LICENSE). Use the lists however you like. They come with no warranty.
