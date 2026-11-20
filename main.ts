// news-image-20261120 entry (Node 22, standard library only).
//
// entry.png sits beside this file: a hand-drawn newspaper infographic
// of the six big stories of Friday 20 November 2026 (draw.py shows how
// it was made; README.md lists the stories and their sources). This
// program just copies that fixed asset to the output directory, so
// the result is the same bytes on every run — nothing is re-rendered,
// and no clock or random value is involved.
//
// When the grader runs outside its container, MAKEFUN_OUTPUT_DIR
// stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';

function main(): void {
  const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
  const source = new URL('./entry.png', import.meta.url);

  // Fail loudly if the asset is missing instead of handing the
  // grader an empty or half-written output file.
  if (!existsSync(source)) {
    throw new Error(
      'entry.png is missing next to main.ts; cannot write /output/entry.png',
    );
  }

  mkdirSync(outDir, { recursive: true });
  const target = join(outDir, 'entry.png');
  copyFileSync(source, target);

  // The copy has to be exact: a short write would silently grade as
  // a broken image, so check the sizes before reporting success.
  const expected = statSync(source).size;
  const written = statSync(target).size;
  if (written !== expected) {
    throw new Error(
      `entry.png copy is incomplete: wrote ${written} of ${expected} bytes to ${target}`,
    );
  }
  console.log(`entry.png (${expected} bytes) copied to ${target}`);
}

main();
