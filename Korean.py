english_to_korean_dict = {
    "hello": "안녕하세요 (annyeonghaseyo)",
    "goodbye": "안녕히 가세요 (annyeonghi gaseyo)",
    "happy": "행복해요 (haengbokhaeyo)",
    "thank you": "감사합니다 (kamsahamnida)",
    "please": "제발 (jebal)",
    "yes": "네 (dae)",
    "of course": "물론이죠 (mullonijyo)",
    "love": "사랑해요 (salanghaeyo)",
    "cat": "고양이 (goyangi)",
    "dog": "개 (gae)",
    "tomorrow": "내일 (naeil)",
    "good afternoon": "좋은 오후 (joeun ohu)",
    "good evening": "좋은 저녁 (joeun jeonyeok)",
    "pleased to meet you": "만나서 반가워요 (mannaseo bangawoyo)",
    "see you soon": "곧 봐요 (god bwayo)",
    "see you later": "나중에 봐요 (najunge bwayo)",
    "see you tomorrow": "내일 봐요 (naeil bwayo)",
    "how are you?": "어떻게 지내세요? (eotteoke jinaeseyo?)"
}

# English to Korean translation function
def translate_korean():
    word = entry_word.get().lower()
    if word in english_to_korean_dict:
        result.set(f"Translation (Korean): {english_to_korean_dict[word]}")
    else:
        result.set("Translation: Not found")

