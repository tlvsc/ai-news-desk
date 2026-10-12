FOOTAGE SEARCH FOR THE AI NEWS DESK HEADLINES, 12 Oct 2026 (Rafi's order: find short real clips we may legally reuse)

WHAT WE NEED
A short video clip (about 6 to 10 seconds is enough; longer is fine, we cut it) that fits one news story, to be shown on the presenter's holographic screen. Think: what would a big news channel put on screen for this story? A clip of the real subject is best; a fitting generic scene (a data centre, a chip factory, a robot working, people on a phone call) is fine. A still image is NOT enough, we need moving video or a GIF with real motion.

LEGAL RULES (strict, nothing is guessed)
1. Use only a clip whose page or repo clearly states a licence that allows reuse: public domain, CC0, CC BY, CC BY-SA, US federal government work, UK Open Government Licence, Apache-2.0, MIT, BSD. Copy the licence name and the URL of the licence statement.
2. NOT usable: YouTube, TikTok, X, news sites (Reuters, AP, BBC and so on), company marketing sites or press kits with no open licence, stock sites that bar redistribution, CC BY-NC or CC BY-ND (flag them as "non-commercial, not safe" and do not download). If you are not sure of the licence, it is NOT usable: say so.
3. Good places: Wikimedia Commons (video files, the file page shows the licence), archive.org (public domain or CC items), NASA and other US government sites, GitHub repos of the company or project that publish their own media under Apache-2.0, MIT or CC (read the LICENSE file), Epoch AI (its own content is CC BY 4.0, check), Flickr items with a CC licence. Pexels and Pixabay are blocked from this machine.
4. A CC BY-SA clip is allowed but write "share-alike" in the notes. A clip with a named real person's face, a readable logo or readable text: allowed to report, but write it in has_faces and has_text_logos.

HOW TO WORK
- Load the web tools first: ToolSearch with query "select:WebSearch,WebFetch". The proxy blocks some hosts; Wikimedia, archive.org, NASA, Flickr and GitHub raw files are reachable. Download with curl -sSL -o FILE URL (never disable TLS checks). Use ffprobe/ffmpeg if present (check with `which ffprobe ffmpeg`) for duration and resolution; if a file is over 20 MB or longer than 30 seconds, cut a clean 10 second piece with ffmpeg and keep the original name plus _cut.
- Save every download under FOOTAGE/clip_NN/ (FOOTAGE is the folder named in your task; NN is the clip number). Media stays out of git and Drive; touch nothing else, delete nothing.
- Per clip: at most 14 tool calls. If you find no clip we may legally reuse, write status "none" and say which sources you tried. A real "none" is a good answer; do not stretch a licence to get a hit.
- Write one JSON file per clip: FOOTAGE/clip_NN/footage.json with: clip, story (one line), status ("found" or "none"), file, source_url (the page), download_url, licence (name), licence_url, credit_label (a short on-screen label such as "Video: Wikimedia Commons, <author> (CC BY 4.0)"), author, size_bytes, duration_s, resolution, has_faces (yes/no and who), has_text_logos (yes/no), md5, notes, sources_tried (list).
- Your final reply: at most 8 short lines, one per clip: status, file name, size, duration, licence, and anything Rafi must know.
