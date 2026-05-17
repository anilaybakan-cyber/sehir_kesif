class CityGuide {
  final Meta meta;
  final List<String> pills;
  final Sections sections;

  CityGuide({required this.meta, required this.pills, required this.sections});

  factory CityGuide.fromJson(Map<String, dynamic> json) => CityGuide(
        meta: Meta.fromJson(json['meta']),
        pills: List<String>.from(json['pills']),
        sections: Sections.fromJson(json['sections']),
      );
}

class Meta {
  final String city, country, language, tagline, colorPrimary, colorLight;
  Meta({required this.city, required this.country, required this.language,
      required this.tagline, required this.colorPrimary, required this.colorLight});
  factory Meta.fromJson(Map<String, dynamic> j) => Meta(
        city: j['city'], country: j['country'], language: j['language'],
        tagline: j['tagline'], colorPrimary: j['color_primary'], colorLight: j['color_light']);
}

class Sections {
  final Overview overview;
  final NeighborhoodsSection neighborhoods;
  final SeasonsSection seasons;
  final FoodSection food;
  final HiddenGemsSection hiddenGems;
  final ChecklistSection checklist;

  Sections({required this.overview, required this.neighborhoods,
      required this.seasons, required this.food,
      required this.hiddenGems, required this.checklist});

  factory Sections.fromJson(Map<String, dynamic> j) => Sections(
        overview: Overview.fromJson(j['overview']),
        neighborhoods: NeighborhoodsSection.fromJson(j['neighborhoods']),
        seasons: SeasonsSection.fromJson(j['seasons']),
        food: FoodSection.fromJson(j['food']),
        hiddenGems: HiddenGemsSection.fromJson(j['hidden_gems']),
        checklist: ChecklistSection.fromJson(j['checklist']),
      );
}

// --- Overview ---
class Overview {
  final String title, intro;
  final LocalWord localWord;
  final List<GuideRule> rules;
  final List<QuickFact> quickFacts;
  final Callout tip;

  Overview({required this.title, required this.intro, required this.localWord,
      required this.rules, required this.quickFacts, required this.tip});

  factory Overview.fromJson(Map<String, dynamic> j) => Overview(
        title: j['title'], intro: j['intro'],
        localWord: LocalWord.fromJson(j['local_word']),
        rules: (j['rules'] as List).map((e) => GuideRule.fromJson(e)).toList(),
        quickFacts: (j['quick_facts'] as List).map((e) => QuickFact.fromJson(e)).toList(),
        tip: Callout.fromJson(j['tip']),
      );
}

class LocalWord {
  final String word, pronunciation, definition;
  LocalWord({required this.word, required this.pronunciation, required this.definition});
  factory LocalWord.fromJson(Map<String, dynamic> j) =>
      LocalWord(word: j['word'], pronunciation: j['pronunciation'], definition: j['definition']);
}

class GuideRule {
  final int number;
  final String title, description;
  GuideRule({required this.number, required this.title, required this.description});
  factory GuideRule.fromJson(Map<String, dynamic> j) =>
      GuideRule(number: j['number'], title: j['title'], description: j['description']);
}

class QuickFact {
  final String icon, label, value, sub;
  QuickFact({required this.icon, required this.label, required this.value, required this.sub});
  factory QuickFact.fromJson(Map<String, dynamic> j) =>
      QuickFact(icon: j['icon'], label: j['label'], value: j['value'], sub: j['sub']);
}

class Callout {
  final String type, label, text;
  Callout({required this.type, required this.label, required this.text});
  factory Callout.fromJson(Map<String, dynamic> j) =>
      Callout(type: j['type'], label: j['label'], text: j['text']);
}

// --- Neighborhoods ---
class NeighborhoodsSection {
  final String title, intro;
  final LocalWord localWord;
  final List<Neighborhood> items;
  final Callout callout;

  NeighborhoodsSection({required this.title, required this.intro,
      required this.localWord, required this.items, required this.callout});

  factory NeighborhoodsSection.fromJson(Map<String, dynamic> j) => NeighborhoodsSection(
        title: j['title'], intro: j['intro'],
        localWord: LocalWord.fromJson(j['local_word']),
        items: (j['items'] as List).map((e) => Neighborhood.fromJson(e)).toList(),
        callout: Callout.fromJson(j['callout']),
      );
}

class Neighborhood {
  final String name, badge, badgeType, description;
  final List<String> tags;
  Neighborhood({required this.name, required this.badge, required this.badgeType,
      required this.description, required this.tags});
  factory Neighborhood.fromJson(Map<String, dynamic> j) => Neighborhood(
        name: j['name'], badge: j['badge'], badgeType: j['badge_type'],
        description: j['description'], tags: List<String>.from(j['tags']));
}

// --- Seasons ---
class SeasonsSection {
  final String title, intro;
  final List<Season> items;
  SeasonsSection({required this.title, required this.intro, required this.items});
  factory SeasonsSection.fromJson(Map<String, dynamic> j) => SeasonsSection(
        title: j['title'], intro: j['intro'],
        items: (j['items'] as List).map((e) => Season.fromJson(e)).toList());
}

class Season {
  final String id, label, name, months, subtitle, description;
  final Callout callout;
  Season({required this.id, required this.label, required this.name,
      required this.months, required this.subtitle, required this.description,
      required this.callout});
  factory Season.fromJson(Map<String, dynamic> j) => Season(
        id: j['id'], label: j['label'], name: j['name'], months: j['months'],
        subtitle: j['subtitle'], description: j['description'],
        callout: Callout.fromJson(j['callout']));
}

// --- Food ---
class FoodSection {
  final String title, intro;
  final LocalWord localWord;
  final List<FoodItem> items;
  final Callout callout;
  FoodSection({required this.title, required this.intro, required this.localWord,
      required this.items, required this.callout});
  factory FoodSection.fromJson(Map<String, dynamic> j) => FoodSection(
        title: j['title'], intro: j['intro'],
        localWord: LocalWord.fromJson(j['local_word']),
        items: (j['items'] as List).map((e) => FoodItem.fromJson(e)).toList(),
        callout: Callout.fromJson(j['callout']));
}

class FoodItem {
  final String icon, name, description, tag;
  FoodItem({required this.icon, required this.name, required this.description, required this.tag});
  factory FoodItem.fromJson(Map<String, dynamic> j) =>
      FoodItem(icon: j['icon'], name: j['name'], description: j['description'], tag: j['tag']);
}

// --- Hidden Gems ---
class HiddenGemsSection {
  final String title, intro;
  final List<HiddenGem> items;
  final Callout callout;
  HiddenGemsSection({required this.title, required this.intro,
      required this.items, required this.callout});
  factory HiddenGemsSection.fromJson(Map<String, dynamic> j) => HiddenGemsSection(
        title: j['title'], intro: j['intro'],
        items: (j['items'] as List).map((e) => HiddenGem.fromJson(e)).toList(),
        callout: Callout.fromJson(j['callout']));
}

class HiddenGem {
  final String rarity, name, description;
  HiddenGem({required this.rarity, required this.name, required this.description});
  factory HiddenGem.fromJson(Map<String, dynamic> j) =>
      HiddenGem(rarity: j['rarity'], name: j['name'], description: j['description']);
}

// --- Checklist ---
class ChecklistSection {
  final String title, completionMessage;
  final List<ChecklistItem> items;
  ChecklistSection({required this.title, required this.completionMessage, required this.items});
  factory ChecklistSection.fromJson(Map<String, dynamic> j) => ChecklistSection(
        title: j['title'], completionMessage: j['completion_message'],
        items: (j['items'] as List).map((e) => ChecklistItem.fromJson(e)).toList());
}

class ChecklistItem {
  final String label, sub;
  ChecklistItem({required this.label, required this.sub});
  factory ChecklistItem.fromJson(Map<String, dynamic> j) =>
      ChecklistItem(label: j['label'], sub: j['sub']);
}
