
characters = {'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
    'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
    'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
    'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
    'ya': 'や',           'yu': 'ゆ',              'yo': 'よ',
    'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
    'wa': 'わ',                                      'wo': 'を',
    'n': 'ん', 'nn': 'ん', 
    'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
    'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
    'da': 'だ', 'dji': 'ぢ', 'dzu': 'づ', 'de': 'で', 'do': 'ど',
    'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
    'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
    'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ',
    'sha': 'しゃ', 'shu': 'しゅ', 'sho': 'しょ',
    'cha': 'ちゃ', 'chu': 'ちゅ', 'cho': 'ちょ',
    'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ',
    'hya': 'ひゃ', 'hyu': 'ひゅ', 'hyo': 'ひょ',
    'mya': 'みゃ', 'myu': 'みゅ', 'myo': 'みょ',
    'rya': 'りゃ', 'ryu': 'りゅ', 'ryo': 'りょ',
    'gya': 'ぎゃ', 'gyu': 'ぎゅ', 'gyo': 'ぎょ',
    'ja': 'じゃ', 'ju': 'じゅ', 'jo': 'じょ',
    'bya': 'びゃ', 'byu': 'びゅ', 'byo': 'びょ',
    'pya': 'ぴゃ', 'pyu': 'ぴゅ', 'pyo': 'ぴょ',

    # Prolonged sound marks and double consonants
    'aa': 'ああ', 'ii': 'いい', 'uu': 'うう', 'ee': 'ええ', 'oo': 'おお',
    'kka': 'っか', 'kki': 'っき', 'kku': 'っく', 'kke': 'っけ', 'kko': 'っこ',
    
    'ssa': 'っさ', 'sshi': 'っし', 'ssu': 'っす', 'sse': 'っせ', 'sso': 'っそ',
    'tta': 'った', 'cchi': 'っち', 'ttsu': 'っつ', 'tte': 'って', 'tto': 'っと',
    'ppa': 'っぱ', 'ppi': 'っぴ', 'ppu': 'っぷ', 'ppe': 'っぺ', 'ppo': 'っぽ',
    'bba': 'っば', 'bbi': 'っび', 'bbu': 'っぶ', 'bbe': 'っべ', 'bbo': 'っぼ',
    'dda': 'っだ', 'ddi': 'っぢ', 'ddu': 'っづ', 'dde': 'っで', 'ddo': 'っど',
    'gga': 'っが', 'ggi': 'っぎ', 'ggu': 'っぐ', 'gge': 'っげ', 'ggo': 'っご',
    'hha': 'っは', 'hhi': 'っひ', 'ffu': 'っふ', 'hhe': 'っへ', 'hho': 'っほ',
    'jja': 'っじゃ', 'jji': 'っじ', 'jju': 'っじゅ', 'jje': 'っじぇ', 'jjo': 'っじょ',
    'kka': 'っか', 'kki': 'っき', 'kku': 'っく', 'kke': 'っけ', 'kko': 'っこ',
    'mma': 'っま', 'mmi': 'っみ', 'mmu': 'っむ', 'mme': 'っめ', 'mmo': 'っも',
    'rra': 'っら', 'rri': 'っり', 'rru': 'っる', 'rre': 'っれ', 'rro': 'っろ',
    'zza': 'っざ', 'jji': 'っじ', 'zzu': 'っず', 'zze': 'っぜ', 'zzo': 'っぞ'
    }

def transcribe(text, characters=characters):
    res = ""
    for e in text.split():
        res += characters[e]
    
    res += "。"
    
    return res



if __name__ == "__main__":
    print(transcribe("ko ni chi wa"))