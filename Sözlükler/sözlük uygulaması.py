# türkçe ingilzice gün uygulaması

days=input("Günleri türkçe yaz:")


tr_en={"pazartesi":"monday","salı":"tuesday","çarşamba":"wednesday","perşembe":"thursday","cuma":"friday","cumartesi":"saturday","pazar":"sunday"}
print("İngilizcesi:",end="")
print(tr_en.get(days,"Bu kelime sözlükte yok"))

