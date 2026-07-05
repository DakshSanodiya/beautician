# Pali Goswami Beauty — website

## Folder structure

```
Beautician-Website/
│
├── index.html
├── style.css
├── script.js
├── download-images.py
├── images/            (fill this in — see below)
└── favicon.ico
```

## 1. Get the photos into `images/`

The `images/` folder is empty right now. Run this once on your computer
(needs internet access):

```
pip install requests pillow
python download-images.py
```

This saves 10 files into `images/` — `bridal.webp`, `party.webp`,
`hd-makeup.webp`, `hair-styling.webp`, `hairspa.webp`, `facial.webp`,
`cleanup.webp`, `waxing.webp`, `threading.webp`, `nail-art.webp` — which
`index.html` already points to. They're free-to-use stock photos from
Pexels. Swap in your own real work photos any time — just keep the
same filenames, or update the `src` paths in `index.html`.

## 2. Edit your real prices

Open `index.html`, search for `class="price"`, and replace the
placeholder amounts and durations with your actual rates.

## 3. Deploy

Any of these work, free of cost:

- **Netlify** — go to app.netlify.com/drop and drag the whole
  `Beautician-Website` folder in. You get a live link immediately.
- **GitHub Pages** — create a repo, upload these files, then turn on
  Pages in the repo settings (Settings → Pages → deploy from `main`
  branch).
- **Vercel** — vercel.com → New Project → drag and drop the folder.

No build step is needed — it's a plain HTML/CSS/JS site.

## Contact button

Every "Book Now" button and the WhatsApp buttons open a chat to
+91 89626 32698 with the service name pre-filled in the message.
