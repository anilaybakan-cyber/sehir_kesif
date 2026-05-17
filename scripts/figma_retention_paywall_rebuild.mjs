/**
 * Figma MCP `use_figma` — "code" alanına TEK PARÇA string olarak yapıştır.
 * fileKey: iXZKRL3h0vBxrj4kW3CJVT (veya kendi dosyan)
 *
 * Düzeltme: layer.appendChild(orb) SONRASI e.layoutPositioning = "ABSOLUTE"
 * (önce absolute yazmak Figma API'de hataya düşüyor, layout dağılıyor.)
 */

export const useFigmaCode = `
await figma.setCurrentPageAsync(figma.root.children[0]);
for (const n of [...figma.currentPage.children]) n.remove();

await figma.loadFontAsync({ family: "Inter", style: "Bold" });
await figma.loadFontAsync({ family: "Inter", style: "Semi Bold" });
await figma.loadFontAsync({ family: "Inter", style: "Regular" });

const COL = {
  bg: { r: 21 / 255, g: 18 / 255, b: 30 / 255 },
  card: { r: 37 / 255, g: 33 / 255, b: 49 / 255 },
  accent: { r: 128 / 255, g: 122 / 255, b: 245 / 255 },
  accentPink: { r: 182 / 255, g: 140 / 255, b: 255 / 255 },
  orange: { r: 1, g: 138 / 255, b: 80 / 255 },
  cyan: { r: 94 / 255, g: 200 / 255, b: 1 },
  white: { r: 1, g: 1, b: 1 },
};

const W = 390;
const H = 844;

const root = figma.createFrame();
root.name = "Retention Paywall — 390×844";
root.layoutMode = "VERTICAL";
root.resize(W, H);
root.primaryAxisSizingMode = "FIXED";
root.counterAxisSizingMode = "FIXED";
root.itemSpacing = 0;
root.fills = [{ type: "SOLID", color: COL.bg }];
root.clipsContent = true;
root.x = 80;
root.y = 80;

const layer = figma.createFrame();
layer.name = "Overlay stack";
layer.layoutMode = "VERTICAL";
layer.resize(W, H);
layer.primaryAxisSizingMode = "FIXED";
layer.counterAxisSizingMode = "FIXED";
layer.layoutAlign = "STRETCH";
layer.itemSpacing = 0;
layer.fills = [];
layer.clipsContent = true;
root.appendChild(layer);

function addOrb(name, ox, oy, size, col, blur, op) {
  const e = figma.createEllipse();
  e.name = name;
  e.resize(size, size);
  e.opacity = op;
  e.fills = [{ type: "SOLID", color: col }];
  e.effects = [{ type: "LAYER_BLUR", radius: blur, visible: true }];
  layer.appendChild(e);
  e.layoutPositioning = "ABSOLUTE";
  e.x = ox;
  e.y = oy;
}

addOrb("Glow L", -75, -110, 280, COL.accent, 70, 0.4);
addOrb("Glow BR", 210, 640, 240, COL.accentPink, 55, 0.32);
addOrb("Glow TR", 260, 140, 160, COL.cyan, 45, 0.22);

const shell = figma.createFrame();
shell.name = "Screen content";
shell.layoutMode = "VERTICAL";
shell.resize(W, H);
shell.primaryAxisSizingMode = "FIXED";
shell.counterAxisSizingMode = "FIXED";
shell.itemSpacing = 0;
shell.fills = [];
layer.appendChild(shell);
shell.layoutPositioning = "ABSOLUTE";
shell.x = 0;
shell.y = 0;

const header = figma.createFrame();
header.name = "Top bar";
header.layoutMode = "HORIZONTAL";
header.primaryAxisSizingMode = "FIXED";
header.counterAxisSizingMode = "FIXED";
header.resize(W, 88);
header.paddingLeft = 20;
header.paddingTop = 50;
header.paddingRight = 20;
header.paddingBottom = 10;
header.counterAxisAlignItems = "CENTER";
header.fills = [];
header.layoutAlign = "STRETCH";

const closeBtn = figma.createFrame();
closeBtn.resize(36, 36);
closeBtn.cornerRadius = 18;
closeBtn.layoutMode = "HORIZONTAL";
closeBtn.primaryAxisAlignItems = "CENTER";
closeBtn.counterAxisAlignItems = "CENTER";
closeBtn.fills = [{ type: "SOLID", color: { r: 0, g: 0, b: 0 }, opacity: 0.45 }];
closeBtn.effects = [
  {
    type: "DROP_SHADOW",
    color: { ...COL.accent, a: 0.25 },
    offset: { x: 0, y: 2 },
    radius: 12,
    spread: 0,
    visible: true,
    blendMode: "NORMAL",
  },
];
const closeTxt = figma.createText();
closeTxt.fontName = { family: "Inter", style: "Bold" };
closeTxt.fontSize = 16;
closeTxt.characters = "×";
closeTxt.fills = [{ type: "SOLID", color: COL.white }];
closeBtn.appendChild(closeTxt);
header.appendChild(closeBtn);
shell.appendChild(header);

const body = figma.createFrame();
body.name = "Main";
body.layoutMode = "VERTICAL";
body.primaryAxisSizingMode = "AUTO";
body.counterAxisSizingMode = "FIXED";
body.layoutGrow = 1;
body.layoutAlign = "STRETCH";
body.primaryAxisAlignItems = "CENTER";
body.counterAxisAlignItems = "CENTER";
body.paddingLeft = 22;
body.paddingRight = 22;
body.paddingTop = 12;
body.paddingBottom = 28;
body.itemSpacing = 18;
body.fills = [];
body.minHeight = 500;

const titleRow = figma.createFrame();
titleRow.layoutMode = "HORIZONTAL";
titleRow.primaryAxisSizingMode = "AUTO";
titleRow.counterAxisSizingMode = "AUTO";
titleRow.itemSpacing = 8;
titleRow.counterAxisAlignItems = "CENTER";
titleRow.primaryAxisAlignItems = "CENTER";
titleRow.fills = [];
const sparkL = figma.createText();
sparkL.fontName = { family: "Inter", style: "Bold" };
sparkL.fontSize = 16;
sparkL.characters = "✦";
sparkL.fills = [{ type: "SOLID", color: COL.accent }];
titleRow.appendChild(sparkL);
const headline = figma.createText();
headline.fontName = { family: "Inter", style: "Bold" };
headline.fontSize = 24;
headline.textAlignHorizontal = "CENTER";
headline.characters = "Çok mu pahalı?\\nAnlıyoruz.";
headline.fills = [{ type: "SOLID", color: COL.white }];
headline.effects = [
  {
    type: "DROP_SHADOW",
    color: { r: 0, g: 0, b: 0, a: 0.65 },
    offset: { x: 0, y: 4 },
    radius: 18,
    spread: 0,
    visible: true,
    blendMode: "NORMAL",
  },
];
titleRow.appendChild(headline);
const sparkR = figma.createText();
sparkR.fontName = { family: "Inter", style: "Bold" };
sparkR.fontSize = 16;
sparkR.characters = "✦";
sparkR.fills = [{ type: "SOLID", color: COL.accentPink }];
titleRow.appendChild(sparkR);
body.appendChild(titleRow);

const pct = figma.createText();
pct.fontName = { family: "Inter", style: "Bold" };
pct.fontSize = 72;
pct.characters = "53%";
pct.fills = [
  {
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 1, g: 0.48, b: 0.72, a: 1 } },
      { position: 0.45, color: { ...COL.accent, a: 1 } },
      { position: 0.72, color: { ...COL.accentPink, a: 1 } },
      { position: 1, color: { ...COL.cyan, a: 1 } },
    ],
    gradientTransform: [
      [1, 0, 0],
      [0, 1, 0],
    ],
  },
];
body.appendChild(pct);

const offLbl = figma.createText();
offLbl.fontName = { family: "Inter", style: "Bold" };
offLbl.fontSize = 17;
offLbl.characters = "İNDİRİM";
offLbl.fills = [{ type: "SOLID", color: COL.white, opacity: 0.92 }];
offLbl.letterSpacing = { unit: "PIXELS", value: 8 };
offLbl.effects = [
  {
    type: "DROP_SHADOW",
    color: { ...COL.accent, a: 0.85 },
    offset: { x: 0, y: 0 },
    radius: 14,
    spread: 0,
    visible: true,
    blendMode: "NORMAL",
  },
];
body.appendChild(offLbl);

const cardWrap = figma.createFrame();
cardWrap.layoutMode = "VERTICAL";
cardWrap.primaryAxisSizingMode = "AUTO";
cardWrap.counterAxisSizingMode = "AUTO";
cardWrap.itemSpacing = 0;
cardWrap.fills = [];
cardWrap.paddingTop = 12;

const badgeRow = figma.createFrame();
badgeRow.layoutMode = "HORIZONTAL";
badgeRow.primaryAxisSizingMode = "FIXED";
badgeRow.counterAxisSizingMode = "AUTO";
badgeRow.resize(346, 42);
badgeRow.primaryAxisAlignItems = "CENTER";
badgeRow.counterAxisAlignItems = "CENTER";
badgeRow.fills = [];
const badge = figma.createFrame();
badge.layoutMode = "HORIZONTAL";
badge.paddingLeft = 14;
badge.paddingRight = 14;
badge.paddingTop = 6;
badge.paddingBottom = 6;
badge.cornerRadius = 20;
badge.primaryAxisSizingMode = "AUTO";
badge.counterAxisSizingMode = "AUTO";
badge.fills = [
  {
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { ...COL.accent, a: 1 } },
      { position: 1, color: { ...COL.accentPink, a: 1 } },
    ],
    gradientTransform: [
      [1, 0, 0],
      [0, 1, 0],
    ],
  },
];
badge.strokes = [{ type: "SOLID", color: COL.white, opacity: 0.35 }];
badge.strokeWeight = 1;
badge.effects = [
  {
    type: "DROP_SHADOW",
    color: { ...COL.accent, a: 0.45 },
    offset: { x: 0, y: 4 },
    radius: 14,
    spread: 0,
    visible: true,
    blendMode: "NORMAL",
  },
];
const badgeTxt = figma.createText();
badgeTxt.fontName = { family: "Inter", style: "Bold" };
badgeTxt.fontSize = 11;
badgeTxt.characters = "%53 İNDİRİM";
badgeTxt.fills = [{ type: "SOLID", color: COL.white }];
badge.appendChild(badgeTxt);
badgeRow.appendChild(badge);
cardWrap.appendChild(badgeRow);

const borderShell = figma.createFrame();
borderShell.layoutMode = "VERTICAL";
borderShell.primaryAxisSizingMode = "AUTO";
borderShell.counterAxisSizingMode = "AUTO";
borderShell.paddingLeft = 1.5;
borderShell.paddingRight = 1.5;
borderShell.paddingTop = 1.5;
borderShell.paddingBottom = 1.5;
borderShell.cornerRadius = 21;
borderShell.fills = [
  {
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { ...COL.accent, a: 0.65 } },
      { position: 0.5, color: { ...COL.accentPink, a: 0.45 } },
      { position: 1, color: { ...COL.orange, a: 0.35 } },
    ],
    gradientTransform: [
      [1, 0, 0],
      [0, 1, 0],
    ],
  },
];

const inner = figma.createFrame();
inner.layoutMode = "VERTICAL";
inner.primaryAxisSizingMode = "AUTO";
inner.counterAxisSizingMode = "AUTO";
inner.paddingLeft = 18;
inner.paddingRight = 18;
inner.paddingTop = 22;
inner.paddingBottom = 18;
inner.itemSpacing = 10;
inner.cornerRadius = 19.5;
inner.fills = [{ type: "SOLID", color: COL.card, opacity: 0.92 }];
inner.strokes = [{ type: "SOLID", color: COL.white, opacity: 0.12 }];
inner.strokeWeight = 1;
inner.effects = [{ type: "BACKGROUND_BLUR", radius: 18, visible: true }];

const lbl = figma.createText();
lbl.fontName = { family: "Inter", style: "Semi Bold" };
lbl.fontSize = 12;
lbl.characters = "Sınırlı süre erişim";
lbl.fills = [{ type: "SOLID", color: COL.accent }];
inner.appendChild(lbl);
const oldP = figma.createText();
oldP.fontName = { family: "Inter", style: "Semi Bold" };
oldP.fontSize = 15;
oldP.characters = "$17.99";
oldP.fills = [{ type: "SOLID", color: COL.white, opacity: 0.48 }];
oldP.textDecoration = "STRIKETHROUGH";
inner.appendChild(oldP);
const newP = figma.createText();
newP.fontName = { family: "Inter", style: "Bold" };
newP.fontSize = 32;
newP.characters = "$9.99";
newP.fills = [{ type: "SOLID", color: COL.white }];
inner.appendChild(newP);
const sub = figma.createText();
sub.fontName = { family: "Inter", style: "Regular" };
sub.fontSize = 12;
sub.characters = "deneme sonrası aylık";
sub.fills = [{ type: "SOLID", color: COL.white, opacity: 0.5 }];
inner.appendChild(sub);
borderShell.appendChild(inner);
cardWrap.appendChild(borderShell);
body.appendChild(cardWrap);

const fine = figma.createText();
fine.fontName = { family: "Inter", style: "Regular" };
fine.fontSize = 11;
fine.textAlignHorizontal = "CENTER";
fine.resize(346, 48);
fine.characters =
  "Uygunluk halinde ücretsiz deneme dahildir — istediğiniz zaman iptal.";
fine.fills = [{ type: "SOLID", color: COL.white, opacity: 0.52 }];
body.appendChild(fine);

const cta = figma.createFrame();
cta.layoutMode = "HORIZONTAL";
cta.primaryAxisSizingMode = "FIXED";
cta.counterAxisSizingMode = "FIXED";
cta.resize(346, 54);
cta.cornerRadius = 22;
cta.primaryAxisAlignItems = "CENTER";
cta.counterAxisAlignItems = "CENTER";
cta.fills = [
  {
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { ...COL.orange, a: 1 } },
      { position: 0.55, color: { ...COL.accent, a: 1 } },
      { position: 1, color: { ...COL.accentPink, a: 1 } },
    ],
    gradientTransform: [
      [1, 0, 0],
      [0, 1, 0],
    ],
  },
];
cta.effects = [
  {
    type: "DROP_SHADOW",
    color: { ...COL.accent, a: 0.42 },
    offset: { x: 0, y: 10 },
    radius: 22,
    spread: 0,
    visible: true,
    blendMode: "NORMAL",
  },
];
const ctaTxt = figma.createText();
ctaTxt.fontName = { family: "Inter", style: "Bold" };
ctaTxt.fontSize = 17;
ctaTxt.characters = "Devam et";
ctaTxt.fills = [{ type: "SOLID", color: COL.white }];
cta.appendChild(ctaTxt);
body.appendChild(cta);

const dismiss = figma.createText();
dismiss.fontName = { family: "Inter", style: "Semi Bold" };
dismiss.fontSize = 13;
dismiss.characters = "Hayır, teşekkürler";
dismiss.fills = [{ type: "SOLID", color: COL.white, opacity: 0.55 }];
body.appendChild(dismiss);

shell.appendChild(body);

figma.viewport.scrollAndZoomIntoView([root]);

return { ok: true, rootId: root.id };
`.trim();
