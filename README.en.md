# Yandex Lyceum

[Русский](README.md) · **English**

[![CI](https://github.com/EDeev/yandex_lyceum/actions/workflows/ci.yml/badge.svg)](https://github.com/EDeev/yandex_lyceum/actions/workflows/ci.yml)

Solutions to the Yandex Lyceum web development course: Flask apps built around the "Mars colonization
mission" storyline, plus organization search via the Yandex Maps API.

**Status:** coursework (Yandex Lyceum, 2022), completed, archived

![Mission applicant form](docs/screenshots/astronaut.png)

**Stack:** Python · Flask · Jinja2 · Flask-WTF · Bootstrap · Yandex Maps API · Pillow

| Folder | Contents |
|---|---|
| `01-flask-html` | Flask and Jinja2 pages: mission promo page, applicant form, planet choice, selection results, photo upload |
| `02-flask-wtf-forms` | Flask-WTF forms: sign-in, training by profession, list of professions, form auto-answer, cabin assignment |
| `03-yandex-maps-search` | finding the nearest organization via the Yandex organization search API and showing a map |

## Running

```bash
pip install -r requirements.txt
cd 01-flask-html && python server.py          # http://127.0.0.1:8080
YANDEX_API_KEY=your_key python 03-yandex-maps-search/main.py
```

`03-yandex-maps-search` needs a Yandex organization search API key in `YANDEX_API_KEY`.

## License

Coursework (Yandex Lyceum, 2021/22). The code is open for study; there is no separate license.

## Author

**Egor Deev** — [GitHub](https://github.com/EDeev) · [Telegram](https://t.me/DeevEgor) · [egor@deev.space](mailto:egor@deev.space)

---

<div align="center">
  <sub>⭐ If you find this project useful, give it a star on GitHub!</sub>
  <p><sub>Made with ❤️ — <a href="https://deev.space">deev.space</a></sub></p>
</div>
