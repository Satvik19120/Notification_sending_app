from plyer import notification

import time

messages = [

    "🕉️ शुभ मौनी अमावस्या! आत्ममंथन और ध्यान के लिए यह उत्तम समय है। 🏞️🙏",

    "🚩 महाकुंभ मेला 2025 की हार्दिक शुभकामनाएं! हर हर गंगे! 🌊",

    "✨ इस मौनी अमावस्या, मौन का पालन करें और आंतरिक शांति पाएं। 🧘🔱🕉️",

    "🔱 गंगा स्नान का विशेष महत्व! पुण्य कमाइए और आत्मा को शुद्ध कीजिए! 🏞️🧘🔱🕉️",

    "🙏 हर हर महादेव! भगवान शिव की कृपा से आपका जीवन मंगलमय हो! 🕉️🧘🔱🕉️"

]


message=""

for m in range(len(messages)-2):

    message+=messages[m]

for i in range(10):

    notification.notify(title="Jai Shree Ram🚩🚩🚩", message=message)
    
    time.sleep(2)