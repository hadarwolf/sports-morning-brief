// Copy the most recent briefs from ../data/briefs into public/briefs so the static
// build serves them. Runs automatically before `next dev` and `next build`.
import { cpSync, existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const KEEP_DAYS = 14; // enough for "what I missed" and the quiz on yesterday's brief

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, "..", "..", "data", "briefs");
const dest = join(here, "..", "public", "briefs");

rmSync(dest, { recursive: true, force: true });
mkdirSync(dest, { recursive: true });

if (!existsSync(join(src, "index.json"))) {
  console.warn(`copy-briefs: no briefs in ${src} yet; the app will show an empty state`);
  writeFileSync(join(dest, "index.json"), JSON.stringify({ latest: null, dates: [] }));
} else {
  const index = JSON.parse(readFileSync(join(src, "index.json"), "utf8"));
  const dates = index.dates.slice(0, KEEP_DAYS);
  for (const date of dates) cpSync(join(src, date), join(dest, date), { recursive: true });
  writeFileSync(join(dest, "index.json"), JSON.stringify({ latest: dates[0] ?? null, dates }));
  console.log(`copy-briefs: copied ${dates.length} brief(s), latest ${dates[0]}`);
}
