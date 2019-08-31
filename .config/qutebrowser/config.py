
# Interface colors
config.source('theme.py')

# Which interfaces to expose via WebRTC.
# Type: String,  Valid values:
#   - all-interfaces: WebRTC has the right to enumerate all interfaces and bind them to discover public interfaces.
#   - default-public-and-private-interfaces: WebRTC should only use the default route used by http. This also exposes the associated default private address. Default route is the route chosen by the OS on a multi-homed endpoint.
#   - default-public-interface-only: WebRTC should only use the default route used by http. This doesn't expose any local addresses.
#   - disable-non-proxied-udp: WebRTC should only use TCP to contact peers or servers unless the proxy server supports UDP. This doesn't expose any local addresses either.
c.content.webrtc_ip_handling_policy = 'default-public-interface-only'

# Mode to use for hints.
# Note: In ´number´ mode you can also type letters from the hinted
# element to filter and reduce the number of elements that are hinted.
# Type: String, Valid values:
#   - number: Use numeric hints.
#   - letter: Use the characters in the `hints.chars` setting.
#   - word: Use hints words based on the html elements and the extra words.
c.hints.mode = 'number'

# Page(s) to open at the start.
# Type: List of FuzzyUrl
c.url.start_pages = ['about:blank']

# Allow websites to request geolocations.
# Type: BoolAsk, Valid values: true, false, ask
c.content.geolocation = False

# Try to pre-fetch DNS entries to speed up browsing.
# Type: Bool
c.content.dns_prefetch = True

# Automatically start playing `<video>` elements.
# Type: Bool
c.content.autoplay = False

# Allow websites to show notifications.
# Type: BoolAsk, Valid values: true, false, ask
c.content.notifications = False

# Position of the tab bar.
# Type: Position,Valid values: top, bottom, left,right
c.tabs.position = 'bottom'

## Remember the last used download directory.
## Type: Bool
c.downloads.location.remember = False

# User agent to send.
# Type: String
# c.content.headers.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# Search engines which can be used via the address bar.
# Type: Dict
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    'ggl': 'http://www.google.com/search?hl=en&source=hp&ie=ISO-8859-l&q={}',
    'yt': 'https://www.youtube.com/results?search_query={}',
    'wiki': 'https://secure.wikimedia.org/wikipedia/en/w/index.php?title=Special%%3ASearch&search={}',
    'gh': 'https://github.com/search?q={}',
    'ghc': 'https://github.com/search?q={}&type=Code',
    'aw': 'http://wiki.archlinux.org/index.php?search={}',
    'pten': 'https://translate.google.com/?&sl=pt&tl=en&q={}',
    'enpt': 'https://translate.google.com/?&sl=en&tl=pt&q={}',
    'ubd': 'https://www.urbandictionary.com/define.php?term={}',
    'def': 'https://wiktionary.org/wiki/{}',
}

# Bindings for normal mode
config.bind('J', 'scroll down')
config.bind('K', 'scroll up')
config.bind('O', 'set-cmd-text -s :open')
config.bind('d', 'tab-prev')
config.bind('f', 'hint all tab')
config.bind('F', 'hint all')
config.bind('j', 'scroll-page 0 1')
config.bind('k', 'scroll-page 0 -1')
config.bind('o', 'set-cmd-text -s :open -t')
config.bind('s', 'tab-next')
config.bind('x', 'tab-close')
# config.bind(',v', 'hint links spawn umpv {hint-url}')
config.bind(',v', 'hint links spawn ~/.local/bin/3rd/umpv {hint-url}')
config.bind(',a', 'hint links spawn mpv --no-video --no-terminal {hint-url}')

# config.bind(',a', 'hint links userscript mpv_audio')
# config.bind(',V', 'hint --rapid links tag-bg spawn ~/.local/bin/umpv {hint-url}')
# config.bind(',r', 'spawn --userscript readability')

# Enable JavaScript for especific web pages.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')
config.set('content.javascript.enabled', True, '*://www.mathsisfun.com/*')
config.set('content.javascript.enabled', True, '*://*.duckduckgo.com/*')
config.set('content.javascript.enabled', True, '*://*.google.com/*')
config.set('content.javascript.enabled', True, '*://translate.google.com/*')
config.set('content.javascript.enabled', True, '*://www.youtube.com/*')
config.set('content.javascript.enabled', True, '*://www.gmail.com/*')
config.set('content.javascript.enabled', True, '*://www.github.com/*')
config.set('content.javascript.enabled', True, '*://www.reddit.com/*')
config.set('content.javascript.enabled', True, '*://twitter.com/*')
config.set('content.javascript.enabled', True, '*://web.telegram.org/*')
config.set('content.javascript.enabled', True, '*://fitlb.com/*')

c.fonts.web.family.fixed = "Noto Sans Mono"
c.fonts.web.family.serif = "Noto Serif"
c.fonts.web.family.standard = "Noto Sans"
c.fonts.statusbar = "11pt Noto Sans"
c.fonts.tabs = "11pt Noto Sans"
c.fonts.downloads = "11pt Noto Sans"
c.fonts.completion.category = "11pt Noto Sans"
c.fonts.completion.entry = "11pt Noto Sans"
c.fonts.hints = "11pt Noto Sans"
c.fonts.keyhint = "11pt Noto Sans"
c.fonts.messages.error = "11pt Noto Sans"
c.fonts.messages.info = "11pt Noto Sans"
c.fonts.messages.warning = "11pt Noto Sans"
c.fonts.monospace = "11pt Noto Sans Mono"
c.fonts.prompts = "11pt Noto Sans"
