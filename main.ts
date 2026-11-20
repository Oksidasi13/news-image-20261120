// news-image-20261120 entry (Node 22, standard library only).
// The image is entry.png beside this file, drawn by hand with PIL from
// news reported on Friday 20 November 2026 (see draw.py for how it was
// made and README.md for the six stories and their sources). The program
// copies it to /output/entry.png, deterministically: the same bytes on
// every run, since the file is copied, never re-rendered.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';

const out = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
// entry.png is a fixed asset in this repository, so copying it is
// byte-identical on every run; no timestamps or randomness are involved.
const src = new URL('./entry.png', import.meta.url);
if (!existsSync(src)) {
  throw new Error('entry.png is missing next to main.ts; cannot write /output/entry.png');
}
mkdirSync(out, { recursive: true });
const dest = join(out, 'entry.png');
copyFileSync(src, dest);
// The copy must be exact: fail loudly rather than hand the grader a
// truncated or partial image if the disk write went wrong.
const srcBytes = statSync(src).size;
const destBytes = statSync(dest).size;
if (destBytes !== srcBytes) {
  throw new Error(
    `entry.png copy is incomplete: wrote ${destBytes} of ${srcBytes} bytes to ${dest}`,
  );
}
console.log(`copied entry.png (${srcBytes} bytes) to ${dest}`);
