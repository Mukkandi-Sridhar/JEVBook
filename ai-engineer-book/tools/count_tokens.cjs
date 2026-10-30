const enc = {o200k: require('gpt-tokenizer/cjs/encoding/o200k_base'), cl100k: require('gpt-tokenizer/cjs/encoding/cl100k_base')};
const texts = JSON.parse(require('fs').readFileSync(process.argv[2],'utf8'));
for (const [k,e] of Object.entries(enc)) for (const t of texts) { const ids=e.encode(t); console.log(k, ids.length, t.length, JSON.stringify(ids.map(i=>e.decode([i])))); }
