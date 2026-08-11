#!/bin/bash
# Wave 2 runner: waits for the wave-1 build chain to finish (agy single-lane
# discipline), then scouts and builds the ten new countries.
cd /home/diablo/book10 || exit 1
# wait for wave 1 (us-2024.tsv is the last link in that chain), max 90 min
for i in $(seq 1 90); do
  [ -s corpus/us-2024.tsv ] && break
  sleep 60
done
echo "[wave2] starting at $(date +%H:%M:%S) (wave1 us table: $( [ -s corpus/us-2024.tsv ] && echo present || echo TIMED OUT — proceeding anyway ))"
./tools/scout_canon2.sh
[ -s notes/scout-canon2.md ] || { echo "wave2 ABORT: scout failed"; exit 1; }
./tools/build_canon.sh mx mx-2024.tsv
./tools/build_canon.sh br br-2024.tsv
./tools/build_canon.sh vn vn-2024.tsv
./tools/build_canon.sh jp jp-2024.tsv
./tools/build_canon.sh be be-2024.tsv
./tools/build_canon.sh au au-2024.tsv
./tools/build_canon.sh ch ch-2024.tsv
./tools/build_canon.sh no no-2024.tsv
./tools/build_canon.sh mn mn-2024.tsv
./tools/build_canon.sh bo bo-2024.tsv
echo "WAVE2 DONE: $(ls corpus/*.tsv | wc -l) tables total"
