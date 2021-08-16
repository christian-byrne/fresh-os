// Fullscreen
window.cryptowatch.disable.fullscreen



window.cryptowatch = { 
    seriesType: 'market', 
    series: { 
        id: '61534', 
        slug: 'KRAKEN:DOGE-USD', 
        symbol: 'kraken:dogeusd', 
        label: 'DOGEUSD', 
        active: true, 
        type: 'market' 
    }, 
    exchange: { 
        slug: 'kraken', 
        id: '4', 
        name: 'Kraken', 
        supports: { 
            trading: true, 
            margin: true, 
            closePosition: false, 
            settlePosition: false, 
            marginForPair: false 
        }, 
        marginActions: [
            "close", 
            "settle"
        ] 
    }, 
    apiErrors: { 
        "3032": "No volume to close position", 
        "400": "Invalid request", 
        "800": "No response from API", 
        "801": "Network problem", 
        "802": "Unauthenticated request", 
        "803": "Request was rate limited", 
        "804": "API key lacking necessary privileges", 
        "805": "API key invalid", 
        "806": "Invalid nonce", 
        "807": "Invalid timestamp", 
        "808": "Invalid passphrase", 
        "809": "Invalid signature", 
        "810": "Timeout", 
        "811": "Exchange API is unavailable", 
        "812": "Invalid anonymous session", 
        "813": "Too many requests queued", 
        "814": "IP address banned by API", 
        "815": "Bad argument passed to API", 
        "816": "Access forbidden to the requested resource", 
        "820": "Internal error", 
        "821": "Unknown error", 
        "822": "Not implemented", 
        "823": "Internal error: bad implementation", 
        "900": "Not enough balance", 
        "901": "Order id is invalid", 
        "902": "Order amount is too low", 
        "903": "Order price is too low", 
        "904": "Order amount is too high", 
        "905": "Order price is too high", 
        "906": "Cannot open position", 
        "907": "Margin allowance exceeded", 
        "908": "Insufficient margin", 
        "909": "Too many open orders", 
        "910": "Too many open positions", 
        "911": "Invalid position", 
        "912": "Invalid arguments", 
        "913": "Invalid price parameter", 
        "914": "Invalid amount parameter", 
        "915": "Price parameter is too precise", 
        "916": "Order price is too low/high", 
        "917": "Order size is too low/high", 
        "918": "Invalid leverage parameter", 
        "919": "Invalid close price parameter", 
        "920": "Invalid lot size", 
        "921": "Invalid expire time", 
        "922": "Unable to fill order completely"
     }, 
     userCanTrade: false, 
     showIntroTour: false, 
     locale: 'en', 
     pair: 'dogeusd', 
     intervalPeriod: { 
         "size": 86400, "offset": 0, "uiSlug": "1d", "apiSlug": "86400", "apiV2Slug": "1d"
     }, 
     intervalPeriods: [
         { "size": 60, "offset": 0, "uiSlug": "1m", "apiSlug": "60", "apiV2Slug": "1m" }, 
         { "size": 180, "offset": 0, "uiSlug": "3m", "apiSlug": "180", "apiV2Slug": "3m" }, 
         { "size": 300, "offset": 0, "uiSlug": "5m", "apiSlug": "300", "apiV2Slug": "5m" }, 
         { "size": 900, "offset": 0, "uiSlug": "15m", "apiSlug": "900", "apiV2Slug": "15m" }, 
         { "size": 1800, "offset": 0, "uiSlug": "30m", "apiSlug": "1800", "apiV2Slug": "30m" }, 
         { "size": 3600, "offset": 0, "uiSlug": "1h", "apiSlug": "3600", "apiV2Slug": "1h" }, 
         { "size": 7200, "offset": 0, "uiSlug": "2h", "apiSlug": "7200", "apiV2Slug": "2h" }, 
         { "size": 14400, "offset": 0, "uiSlug": "4h", "apiSlug": "14400", "apiV2Slug": "4h" }, 
         { "size": 21600, "offset": 0, "uiSlug": "6h", "apiSlug": "21600", "apiV2Slug": "6h" }, 
         { "size": 43200, "offset": 0, "uiSlug": "12h", "apiSlug": "43200", "apiV2Slug": "12h" }, 
         { "size": 86400, "offset": 0, "uiSlug": "1d", "apiSlug": "86400", "apiV2Slug": "1d" }, 
         { "size": 259200, "offset": 0, "uiSlug": "3d", "apiSlug": "259200", "apiV2Slug": "3d" }, 
         { "size": 604800, "offset": 0, "uiSlug": "1w", "apiSlug": "604800", "apiV2Slug": "1w" }, 
         { "size": 604800, "offset": 345600, "uiSlug": "1w_Monday", "apiSlug": "604800_Monday", "apiV2Slug": "1w" }
    ], 
    currencyPair: { 
        slug: 'dogeusd', 
        base: 'DOGE', 
        quote: 'USD'
    }, 
    device: { 
        isPhone: false, 
        isTablet: false, 
        mobileMode: { 
            mobileSite: true, 
            desktopSite: false } 
        }, 
    disable: { 
        "header": false, 
        "exchangeLink": true, 
        "orderBookFeed": false, 
        "dataPointsFeed": false, 
        "userAccounts": true, 
        "trading": false, 
        "currencyOverview": false, 
        "marketNavigation": false, 
        "notifications": false, 
        "fullscreen": false, 
        "embed": true, 
        "hotkeys": false, 
        "changelog": true, 
        "settings": { 
            "all": false, 
            "inline": false, 
            "helpLinks": false, 
            "fiatPreference": false, 
            "myActivity": false, 
            "performance": false, 
            "colorScheme": false 
        } 
    }, 
    cwChartChrome: { 
        contract: "", 
        contractSeries: null, 
        externalURL: "https://www.kraken.com", 
        externalURLShort: "kraken.com", 
        isFutures: false, 
        navLinkHref: "", 
        otherContractsOffered: false, 
        periodUiSlug: "1D", 
        seriesSlug: 'KRAKEN:DOGE-USD', } 
}