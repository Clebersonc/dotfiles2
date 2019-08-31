colors = {

    'color0': '#222222',
    'color1': '#303030',
    'color2': '#333333',
    'color3': '#424242',

    'color4': '#f1f1f1',
    'color5': '#e5e5e5',
    'color6': '#cccccc',

    'color7': '#8fbcbb',
    'color8': '#727272',
    'color9': '#81a1c1',
    'color10': '#5e81ac',

    'color11': '#bf616a',
    'color12': '#a89c14',
    'color13': '#f3e430',
    'color14': '#5fd7a7',
    'color15': '#6855de',
}

## Background color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.bg = colors['color0']

## Bottom border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.bottom = colors['color0']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.top = colors['color0']

## Foreground color of completion widget category headers.
## Type: QtColor
c.colors.completion.category.fg = colors['color5']

## Background color of the completion widget for even rows.
## Type: QssColor
c.colors.completion.even.bg = colors['color1']

## Background color of the completion widget for odd rows.
## Type: QssColor
c.colors.completion.odd.bg = colors['color1']

## Text color of the completion widget.
## Type: QtColor
c.colors.completion.fg = colors['color4']

## Background color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.bg = colors['color3']

## Bottom border color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.border.bottom = colors['color3']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.item.selected.border.top = colors['color3']

## Foreground color of the selected completion item.
## Type: QtColor
c.colors.completion.item.selected.fg = colors['color6']

## Foreground color of the matched text in the completion.
## Type: QssColor
c.colors.completion.match.fg = colors['color13']

## Color of the scrollbar in completion view
## Type: QssColor
c.colors.completion.scrollbar.bg = colors['color1']

## Color of the scrollbar handle in completion view.
## Type: QssColor
c.colors.completion.scrollbar.fg = colors['color5']

## Background color for the download bar.
## Type: QssColor
c.colors.downloads.bar.bg = colors['color0']

## Background color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.bg = colors['color11']

## Foreground color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.fg = colors['color5']

## Color gradient stop for download backgrounds.
## Type: QtColor
c.colors.downloads.stop.bg = colors['color15']

## Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'

## Background color for hints. Note that you can use a `rgba(...)` value
## for transparency.
## Type: QssColor
c.colors.hints.bg = colors['color13']

## Font color for hints.
## Type: QssColor
c.colors.hints.fg = colors['color0']

## Font color for the matched part of hints.
## Type: QssColor
c.colors.hints.match.fg = colors['color10']

## Background color of the keyhint widget.
## Type: QssColor
c.colors.keyhint.bg = colors['color1']

## Text color for the keyhint widget.
## Type: QssColor
c.colors.keyhint.fg = colors['color5']

## Highlight color for keys to complete the current keychain.
## Type: QssColor
c.colors.keyhint.suffix.fg = colors['color13']

## Background color of an error message.
## Type: QssColor
c.colors.messages.error.bg = colors['color11']

## Border color of an error message.
## Type: QssColor
c.colors.messages.error.border = colors['color11']

## Foreground color of an error message.
## Type: QssColor
c.colors.messages.error.fg = colors['color5']

## Background color of an info message.
## Type: QssColor
c.colors.messages.info.bg = colors['color8']

## Border color of an info message.
## Type: QssColor
c.colors.messages.info.border = colors['color8']

## Foreground color an info message.
## Type: QssColor
c.colors.messages.info.fg = colors['color5']

## Background color of a warning message.
## Type: QssColor
c.colors.messages.warning.bg = colors['color12']

## Border color of a warning message.
## Type: QssColor
c.colors.messages.warning.border = colors['color12']

## Foreground color a warning message.
## Type: QssColor
c.colors.messages.warning.fg = colors['color5']

## Background color for prompts.
## Type: QssColor
c.colors.prompts.bg = colors['color2']

# ## Border used around UI elements in prompts.
# ## Type: String
c.colors.prompts.border = '1px solid ' + colors['color0']

## Foreground color for prompts.
## Type: QssColor
c.colors.prompts.fg = colors['color5']

## Background color for the selected item in filename prompts.
## Type: QssColor
c.colors.prompts.selected.bg = colors['color3']

## Background color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.bg = colors['color15']

## Foreground color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.fg = colors['color5']

## Background color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.bg = colors['color15']

## Foreground color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.fg = colors['color5']

## Background color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.bg = colors['color2']

## Foreground color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.fg = colors['color5']

## Background color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.bg = colors['color2']

## Foreground color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.fg = colors['color5']

## Background color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.bg = colors['color14']

## Foreground color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.fg = colors['color1']

## Background color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.bg = colors['color0']

## Foreground color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.fg = colors['color5']

## Background color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.bg = colors['color10']

## Foreground color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.fg = colors['color5']

## Background color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.bg = colors['color3']

## Foreground color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.fg = colors['color5']

## Background color of the progress bar.
## Type: QssColor
c.colors.statusbar.progress.bg = colors['color5']

## Foreground color of the URL in the statusbar on error.
## Type: QssColor
c.colors.statusbar.url.error.fg = colors['color11']

## Default foreground color of the URL in the statusbar.
## Type: QssColor
c.colors.statusbar.url.fg = colors['color5']

## Foreground color of the URL in the statusbar for hovered links.
## Type: QssColor
c.colors.statusbar.url.hover.fg = colors['color8']

## Foreground color of the URL in the statusbar on successful load
## (http).
## Type: QssColor
c.colors.statusbar.url.success.http.fg = colors['color5']

## Foreground color of the URL in the statusbar on successful load
## (https).
## Type: QssColor
c.colors.statusbar.url.success.https.fg = colors['color14']

## Foreground color of the URL in the statusbar when there's a warning.
## Type: QssColor
c.colors.statusbar.url.warn.fg = colors['color12']

## Background color of the tab bar.
## Type: QtColor
c.colors.tabs.bar.bg = colors['color3']

## Background color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.bg = colors['color3']

## Foreground color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.fg = colors['color5']

## Color for the tab indicator on errors.
## Type: QtColor
c.colors.tabs.indicator.error = colors['color11']

## Color gradient start for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.start = colors['violet']

## Color gradient end for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.stop = colors['orange']

## Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

## Background color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.bg = colors['color3']

## Foreground color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.fg = colors['color5']

# ## Background color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.bg = colors['color0']

# ## Foreground color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.fg = colors['color5']

# ## Background color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.bg = colors['color0']

# ## Foreground color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.fg = colors['color5']

## Background color for webpages if unset (or empty to use the theme's
## color)
## Type: QtColor
# c.colors.webpage.bg = 'white'
