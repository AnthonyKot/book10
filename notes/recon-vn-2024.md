# Vietnam 2024 reconciliation

## Summary

- Rows: 107 before, 107 after (header excluded).
- Edits: 33 `subject_era` cells and 6 `memorize` cells across 38 rows.
- Quarantine: 0 rows; the blind-confirm report flagged no unsupported rows, and the saved curriculum copies confirmed the in-scope entries under their Vietnamese, abbreviated, or transliterated title/author forms.

The defining curriculum distinguishes compulsory works, compulsory choices, and suggested materials from its grade-wide memorization outcomes. Those outcomes require an unspecified quantity of selected or favorite passages/poems; they do not identify any listed work. Systemic ruling: compulsory status, permission to teach a long work through excerpts, closed-book assessment, and general recitation culture do not establish a work-specific mandate, so `memorize = yes/excerpt` is used only when the defining document explicitly names the text or a passage/quantity tied to it. No Vietnam row meets that test.

The curriculum evidence was rechecked in `resources/thong_tu_32_2018_ngu_van.txt`, its PDF/web copies, and `resources/vn_curriculum.pdf`. The compulsory list appears in section V; the author/national-literature choice entries follow it; and the named suggested texts appear in section IX. Searches included Vietnamese titles, unaccented/transliterated forms, English glosses, and abbreviated author forms such as A. Doyle, J. Rousseau, Lỗ Tấn/Lu Xun, and Nguyễn Ái Quốc/Hồ Chí Minh.

## Change log

TSV line numbers below include the header as line 1.

- Line 2, `memorize`: `yes` -> `no` — *Nam quốc sơn hà* is compulsory, but the document assigns only an unspecified grade-wide selection of favorite poems/passages for memorization.
- Line 3, `memorize`: `excerpt` -> `no` — *Hịch tướng sĩ* has no named passage or quantity mandated for learning by heart.
- Line 4, `memorize`: `excerpt` -> `no` — *Bình Ngô đại cáo* has no named passage or quantity mandated for learning by heart.
- Line 5, `subject_era`: `feudalism-justice?` -> `early-modern-ming-china/trafficking-and-feudal-patriarchy` — the narrative is set in Ming China and represents Kiều's coerced sale, sexual exploitation, and patriarchal injustice.
- Line 5, `memorize`: `excerpt` -> `no` — permission to teach the long work through excerpts is not a mandate to memorize an excerpt.
- Line 6, `memorize`: `excerpt` -> `no` — *Văn tế nghĩa sĩ Cần Giuộc* has no named passage or quantity mandated for learning by heart.
- Line 7, `memorize`: `yes` -> `no` — compulsory status for the declaration does not supply a text-specific learning-by-heart mandate.
- Line 13, `subject_era`: `le-dynasty-building?` -> `various/unspecified` — the open Nguyễn Trãi poetry/essay choice names no work and therefore fixes no represented era.
- Line 14, `subject_era`: `feudalism?` -> `various/unspecified` — the open Nguyễn Du Chinese-script poetry choice names no poem and therefore fixes no common subject.
- Line 15, `subject_era`: `feudal-patriarchy?` -> `various/unspecified` — the open Hồ Xuân Hương poetry choice does not make patriarchy the necessary subject of the selected poem.
- Line 16, `subject_era`: `anti-french-resistance` -> `various/unspecified` — the open Nguyễn Đình Chiểu poetry choice can include moral narratives as well as resistance verse.
- Line 17, `subject_era`: `french-colonialism?` -> `various/unspecified` — the open Nguyễn Khuyến poetry choice includes lyric subjects not uniformly about colonialism.
- Line 18, `subject_era`: `anti-french-resistance` -> `various/unspecified` — the unspecified Nguyễn Ái Quốc–Hồ Chí Minh stories and poems span colonialism, imprisonment, revolution, and war.
- Line 19, `subject_era`: `1930s-famine/peasantry?` -> `various/unspecified` — the unspecified Nam Cao fiction choice also includes urban and intellectual life and does not uniformly concern famine or peasants.
- Line 20, `subject_era`: `colonial-bourgeoisie?` -> `various/unspecified` — the unspecified Vũ Trọng Phụng novels/reportage span distinct subjects.
- Line 21, `subject_era`: `pre-1945-romanticism?` -> `various/unspecified` — “pre-1945” limits eligible composition dates but names no represented era or wound.
- Line 22, `subject_era`: `indochina-war/socialism?` -> `various/unspecified` — the open Tố Hữu selection crosses both sides of 1945 and names no poem.
- Line 23, `subject_era`: `post-1945-reconstruction?` -> `various/unspecified` — the open Nguyễn Tuân stories/ký choice spans pre- and post-1945 work.
- Line 24, `subject_era`: `august-revolution-war` -> `various/unspecified` — Nguyễn Huy Tưởng's unnamed play choice ranges from early-modern court history to twentieth-century revolution.
- Line 25, `subject_era`: `subsidy-era-social-critique?` -> `various/unspecified` — the curriculum names no Lưu Quang Vũ play, so subsidy-era critique is not assured.
- Line 29, `subject_era`: `antiquity?` -> `various/unspecified` — the Greek-literature quota names a national literature, not an ancient work or period.
- Line 33, `subject_era`: `antiquity?` -> `various/unspecified` — the Indian-literature quota is not confined to an ancient work or period.
- Line 35, `subject_era`: `none/romance` -> `early-20th-c-new-york/artist-poverty-and-illness` — *The Last Leaf* represents impoverished Greenwich Village artists, pneumonia, friendship, and sacrifice rather than romance.
- Line 38, `subject_era`: `contemporary-delta-life?` -> `contemporary-mountain-village/poverty-and-family-abandonment` — Khờ waits in a poor mountain community for the mother who abandoned him, not in the Mekong Delta.
- Line 40, `subject_era`: `WWII-humanism?` -> `none/philosophical-fable-and-friendship` — *The Little Prince* represents an atemporal planetary fable; WWII is composition context.
- Line 43, `subject_era`: `1930s-famine/peasantry?` -> `french-colonial-rural-poverty` — *Lão Hạc* depicts colonial-era peasant poverty and dispossession, not the 1945 famine.
- Line 47, `subject_era`: `victorian-crime?` -> `late-victorian/edwardian-britain-crime` — the generic Holmes entry spans late-Victorian, Edwardian, and pre-WWI settings.
- Line 52, `subject_era`: `anti-french-resistance` -> `1945-famine/anti-french-war-memory` — the remembered childhood includes both the 1945 famine and subsequent resistance-war separation.
- Line 55, `subject_era`: `17th-c-fable?` -> `none/moral-fable` — the seventeenth century is La Fontaine's composition period, while the represented animal world is timeless.
- Line 56, `subject_era`: `none/romance` -> `none/choice-and-regret` — Frost's lyric concerns choice and retrospective self-narration, not romantic love.
- Line 57, `subject_era`: `pre-1945-romanticism?` -> `none/autumn-transience-and-loss` — the poem represents autumnal change, loneliness, and loss; pre-1945 Romanticism is literary context.
- Line 60, `subject_era`: `french-colonialism?` -> `french-colonialism/none-personal-grief` — *Hội Tây* satirizes colonial spectacle, while *Khóc Dương Khuê* is a personal elegy.
- Line 69, `subject_era`: `post-war-contemplation?` -> `none/nature-and-seasonal-transition` — the poem observes late summer becoming autumn; its postwar date is not its subject.
- Line 72, `subject_era`: `pre-1945-romanticism?` -> `mythic-fairyland/farewell` — the poem represents a legendary departure from Thiên Thai fairyland, not its literary period.
- Line 82, `subject_era`: `enlightenment?` -> `none/walking-freedom-and-education` — the excerpt argues for walking as free, embodied education; the Enlightenment is intellectual context.
- Line 84, `subject_era`: `1911-chinese-revolution?` -> `late-qing/1911-revolution/early-republic-social-crisis` — the grouped stories range from late-Qing repression through the 1911 Revolution to early-Republic rural disillusionment.
- Line 87, `subject_era`: `post-war-renovation?` -> `anti-us-war/postwar-renovation` — one grouped story is set during the anti-US war, while the others represent postwar ethical and aesthetic reassessment.
- Line 97, `subject_era`: `anti-us-war` -> `first-indochina-war-in-laos/anti-us-war` — the grouped alternatives cover both the earlier anti-French Lao resistance and the later anti-US war.
- Line 98, `subject_era`: `hanoi-culture-renovation?` -> `1945-revolution/anti-us-war/postwar-doi-moi-hanoi` — the protagonist's life and Hanoi's changes run from the 1945 revolution through wartime into Đổi Mới.

## Quarantine

None. No row identified by the blind-confirm report was absent from every saved defining document after the variant-title/author search.
