import re
from collections import defaultdict

# Leer el archivo de logs
with open('C:\\Users\\Tatiana\\Downloads\\access.log.txt', 'r', encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()

# Expresión regular para extraer el User-Agent (navegador)
user_agent_regex = r'"([^"]+)"\s*$'

# Diccionario para contar los navegadores
browser_count = defaultdict(int)

for line in lines:
    match = re.findall(user_agent_regex, line)
    if match:
        user_agent = match[-1]  # Último campo entre comillas

        # Clasificación extendida de navegadores y bots
        if "Googlebot" in user_agent:
            browser = "Googlebot"
        elif "Baiduspider" in user_agent:
            browser = "Baiduspider"
        elif "Feedfetcher" in user_agent or "FeedBurner" in user_agent or "Feedbin" in user_agent:
            browser = "FeedFetcher"
        elif "archive.org_bot" in user_agent:
            browser = "Internet Archive Bot"
        elif "Dalvik" in user_agent:
            browser = "Android Dalvik"
        elif "UniversalFeedParser" in user_agent:
            browser = "FeedParser"
        elif "Tiny Tiny RSS" in user_agent:
            browser = "Tiny Tiny RSS"
        elif "Chrome" in user_agent and "Safari" in user_agent:
            browser = "Chrome"
        elif "Firefox" in user_agent:
            browser = "Firefox"
        elif "Safari" in user_agent and "Chrome" not in user_agent:
            browser = "Safari"
        elif "MSIE" in user_agent or "Trident" in user_agent:
            browser = "Internet Explorer"
        elif "Opera" in user_agent:
            browser = "Opera"
        else:
            browser = "Otro"

        browser_count[browser] += 1

# Mostrar los resultados
print("Conteo de navegadores y bots encontrados en los logs:\n")
for browser, count in sorted(browser_count.items(), key=lambda x: -x[1]):
    print(f"{browser}: {count}")
