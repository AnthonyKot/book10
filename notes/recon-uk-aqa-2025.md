# UK AQA 2025 reconciliation

Row numbers below are the original data-row numbers in `corpus/uk-aqa-2025.tsv`; the header is excluded.

## Summary

- Rows: 73 before -> 73 after.
- Era edits: 17 disputed `subject_era` values corrected to the work's represented subject or setting.
- Memorize edits: 73 values changed from `excerpt` -> `no`.
- Quarantined rows: 0; the renewed defining-document search supported every disputed row.

The receipt search covered the saved AQA specification, AQA schemes of work, and the saved AQA/Collins *Worlds and Lives* teacher guide. It searched exact titles and author/title spelling variants; for the five extraction mismatches it also checked punctuation, curly/straight apostrophes, subtitle omissions, and PDF line-break variants (`The Curious Incident...`, `Sonnet 29`, `Mother Any Distance`, `Extract from, The Prelude`, and `With Birds You’re Never Lonely`). Transliteration was not applicable to this Latin-script list. Every disputed work was found, so no row was moved to quarantine.

## Systemic memorize ruling

`yes` or `excerpt` requires an explicit defining-document mandate to learn the named text, a named excerpt, or a stated quantity of texts by heart at this level. The AQA specification says that all assessments are closed book, supplies the Paper 1 extracts and the named Paper 2 poem, and requires textual references or quotations; it never mandates learning any named text or stated quantity of texts by heart. Closed-book assessment, implied quote-learning, and general recitation culture therefore do not qualify. All 73 rows are `no`.

## Change log

### Subject era

- Row 11, Mary Shelley, *Frankenstein* — `subject_era`: `19th-c-scientific-ethics` -> `late-18th-c-europe/scientific-creation`; the narrative chronology is late eighteenth-century Europe, not the novel's nineteenth-century publication period.
- Row 23, AQA Anthology, *Telling Tales* — `subject_era`: `20th-c-social-realism` -> `various-20th/21st-c/no-single-era`; the seven stories have multiple settings and concerns rather than one social-realist period.
- Row 31, Robert Browning, *Porphyria's Lover* — `subject_era`: `victorian-psychological-pathology?` -> `none/intimate-partner-violence`; the represented murder has no fixed historical setting and is not about a specifically Victorian wound.
- Row 33, Thomas Hardy, *Neutral Tones* — `subject_era`: `victorian-disillusionment` -> `none/failed-romance`; the poem represents a relationship ending without locating it in a Victorian historical period.
- Row 37, Charles Causley, *Eden Rock* — `subject_era`: `mid-20th-c-memory-bereavement` -> `none/family-memory-bereavement`; the visionary encounter with dead parents does not establish a mid-twentieth-century setting.
- Row 50, Seamus Heaney, *Storm on the Island* — `subject_era`: `northern-ireland-troubles?` -> `20th-c-rural-ireland/natural-threat`; the poem directly represents an island community facing a storm, while a Troubles reading remains an unconfirmed allegory.
- Row 51, Ted Hughes, *Bayonet Charge* — `subject_era`: `WWI-trench-warfare?` -> `20th-c-battle/war-unspecified`; the poem depicts a soldier charging in battle but names neither a war nor a trench setting.
- Row 53, Jane Weir, *Poppies* — `subject_era`: `iraq-afghanistan-war-bereavement` -> `contemporary-war-home-front/bereavement`; the poem represents a contemporary military departure and maternal loss but deliberately leaves the conflict and the son's fate unspecified.
- Row 55, Imtiaz Dharker, *Tissue* — `subject_era`: `contemporary-borders-conflict` -> `none/paper-power-human-fragility`; maps and borders are images in a meditation on paper, power, and mortality, not a particular contemporary conflict.
- Row 56, Carol Rumens, *The Emigree* — `subject_era`: `contemporary-exile-displacement` -> `unspecified-authoritarian-homeland/exile`; the poem intentionally withholds the country and period while representing exile from an oppressive homeland.
- Row 59, William Wordsworth, *Lines Written in Early Spring* — `subject_era`: `romanticism-french-revolution-aftermath?` -> `industrial-revolution/nature-human-harm`; the poem laments what humanity has made of itself and the saved AQA-linked guide connects that concern to industrialisation, not specifically to the French Revolution or merely to Romantic composition context.
- Row 61, Emily Brontë, *Shall earth no more inspire thee* — `subject_era`: `victorian-isolation-nature` -> `none/nature-solace-isolation`; the poem offers nature as solace for private grief without depicting a specifically Victorian historical wound.
- Row 65, Shamshad Khan, *pot* — `subject_era`: `contemporary-heritage-identity` -> `colonial-looting/2000s-guantanamo-detention`; the poem directly represents colonial removal and repatriation and explicitly links the captive pot to detention without charge.
- Row 66, Seni Seneviratne, *A Wider View* — `subject_era`: `20th-c-sri-lankan-heritage` -> `1869-industrial-leeds/migrant-labour`; its historical action is the ancestor's factory labour in Leeds in 1869, joined to a present-day descendant's view.
- Row 67, Liz Berry, *Homing* — `subject_era`: `contemporary-black-country-dialect-identity` -> `20th-c-black-country/linguistic-stigma`; the poem looks back on a dead relative's childhood punishment and lifelong suppression of Black Country speech.
- Row 69, Louisa Adjoa Parker, *The Jewellery Maker* — `subject_era`: `contemporary-artisan-identity` -> `unspecified/artisan-poverty`; the poem foregrounds inherited skilled labour and economic hardship while leaving period and place unstated.
- Row 72, Grace Nichols, *Like an Heiress* — `subject_era`: `post-colonial-caribbean-identity` -> `contemporary-guyana/pollution-climate-change`; heritage frames the return to Guyana, but the represented wound is present-day pollution and the planet's climate future.

### Memorize

- Row 1, William Shakespeare, *Macbeth* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 2, William Shakespeare, *Romeo and Juliet* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 3, William Shakespeare, *The Tempest* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 4, William Shakespeare, *The Merchant of Venice* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 5, William Shakespeare, *Much Ado About Nothing* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 6, William Shakespeare, *Julius Caesar* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 7, Robert Louis Stevenson, *The Strange Case of Dr Jekyll and Mr Hyde* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 8, Charles Dickens, *A Christmas Carol* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 9, Charles Dickens, *Great Expectations* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 10, Charlotte Brontë, *Jane Eyre* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 11, Mary Shelley, *Frankenstein* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 12, Jane Austen, *Pride and Prejudice* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 13, Sir Arthur Conan Doyle, *The Sign of Four* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 14, J.B. Priestley, *An Inspector Calls* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 15, Willy Russell, *Blood Brothers (musical version)* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 16, Alan Bennett, *The History Boys* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 17, Dennis Kelly, *DNA* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 18, Simon Stephens, *The Curious Incident of the Dog in the Night-Time (play script)* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 19, Shelagh Delaney, *A Taste of Honey* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 20, Chinonyerem Odimba, *Princess & The Hustler* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 21, Winsome Pinnock, *Leave Taking* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 22, William Golding, *Lord of the Flies* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 23, AQA Anthology, *Telling Tales* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 24, George Orwell, *Animal Farm* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 25, Kazuo Ishiguro, *Never Let Me Go* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 26, Meera Syal, *Anita and Me* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 27, Stephen Kelman, *Pigeon English* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 28, Kit de Waal, *My Name is Leon* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 29, Lord Byron, *When We Two Parted* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 30, Percy Bysshe Shelley, *Love's Philosophy* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 31, Robert Browning, *Porphyria's Lover* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 32, Elizabeth Barrett Browning, *Sonnet 29 – 'I think of thee!'* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 33, Thomas Hardy, *Neutral Tones* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 34, Maura Dooley, *Letters from Yorkshire* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 35, Charlotte Mew, *The Farmer's Bride* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 36, C. Day Lewis, *Walking Away* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 37, Charles Causley, *Eden Rock* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 38, Seamus Heaney, *Follower* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 39, Simon Armitage, *Mother, Any Distance* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 40, Carol Ann Duffy, *Before You Were Mine* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 41, Owen Sheers, *Winter Swans* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 42, Daljit Nagra, *Singh Song!* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 43, Andrew Waterhouse, *Climbing My Grandfather* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 44, Percy Bysshe Shelley, *Ozymandias* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 45, William Blake, *London* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 46, William Wordsworth, *Extract from The Prelude* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 47, Robert Browning, *My Last Duchess* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 48, Alfred Lord Tennyson, *The Charge of the Light Brigade* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 49, Wilfred Owen, *Exposure* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 50, Seamus Heaney, *Storm on the Island* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 51, Ted Hughes, *Bayonet Charge* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 52, Simon Armitage, *Remains* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 53, Jane Weir, *Poppies* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 54, Carol Ann Duffy, *War Photographer* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 55, Imtiaz Dharker, *Tissue* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 56, Carol Rumens, *The Emigree* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 57, Beatrice Garland, *Kamikaze* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 58, John Agard, *Checking Out Me History* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 59, William Wordsworth, *Lines Written in Early Spring* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 60, Percy Bysshe Shelley, *England in 1819* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 61, Emily Brontë, *Shall earth no more inspire thee* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 62, George Eliot, *In a London Drawingroom* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 63, James Berry, *On an Afternoon Train from Purley to Victoria, 1955* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 64, Raman Mundair, *Name Journeys* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 65, Shamshad Khan, *pot* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 66, Seni Seneviratne, *A Wider View* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 67, Liz Berry, *Homing* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 68, Imtiaz Dharker, *A Century Later* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 69, Louisa Adjoa Parker, *The Jewellery Maker* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 70, Raymond Antrobus, *With Birds You're Never Lonely* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 71, Roger Robinson, *A Portable Paradise* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 72, Grace Nichols, *Like an Heiress* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).
- Row 73, Caleb Femi, *Thirteen* — `memorize`: `excerpt` -> `no`; no explicit by-heart mandate (systemic ruling above).

### Quarantine moves

None.

## Quarantine

No rows were quarantined.
