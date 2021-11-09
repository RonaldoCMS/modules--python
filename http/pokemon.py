# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = pokedex_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, Dict, Optional, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


@dataclass
class Species:
    name: str
    url: str

    @staticmethod
    def from_dict(obj: Any) -> 'Species':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        url = from_str(obj.get("url"))
        return Species(name, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["url"] = from_str(self.url)
        return result


@dataclass
class Ability:
    ability: Species
    is_hidden: bool
    slot: int

    @staticmethod
    def from_dict(obj: Any) -> 'Ability':
        assert isinstance(obj, dict)
        ability = Species.from_dict(obj.get("ability"))
        is_hidden = from_bool(obj.get("is_hidden"))
        slot = from_int(obj.get("slot"))
        return Ability(ability, is_hidden, slot)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ability"] = to_class(Species, self.ability)
        result["is_hidden"] = from_bool(self.is_hidden)
        result["slot"] = from_int(self.slot)
        return result


@dataclass
class GameIndex:
    game_index: int
    version: Species

    @staticmethod
    def from_dict(obj: Any) -> 'GameIndex':
        assert isinstance(obj, dict)
        game_index = from_int(obj.get("game_index"))
        version = Species.from_dict(obj.get("version"))
        return GameIndex(game_index, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["game_index"] = from_int(self.game_index)
        result["version"] = to_class(Species, self.version)
        return result


@dataclass
class VersionGroupDetail:
    level_learned_at: int
    move_learn_method: Species
    version_group: Species

    @staticmethod
    def from_dict(obj: Any) -> 'VersionGroupDetail':
        assert isinstance(obj, dict)
        level_learned_at = from_int(obj.get("level_learned_at"))
        move_learn_method = Species.from_dict(obj.get("move_learn_method"))
        version_group = Species.from_dict(obj.get("version_group"))
        return VersionGroupDetail(level_learned_at, move_learn_method, version_group)

    def to_dict(self) -> dict:
        result: dict = {}
        result["level_learned_at"] = from_int(self.level_learned_at)
        result["move_learn_method"] = to_class(Species, self.move_learn_method)
        result["version_group"] = to_class(Species, self.version_group)
        return result


@dataclass
class Move:
    move: Species
    version_group_details: List[VersionGroupDetail]

    @staticmethod
    def from_dict(obj: Any) -> 'Move':
        assert isinstance(obj, dict)
        move = Species.from_dict(obj.get("move"))
        version_group_details = from_list(VersionGroupDetail.from_dict, obj.get("version_group_details"))
        return Move(move, version_group_details)

    def to_dict(self) -> dict:
        result: dict = {}
        result["move"] = to_class(Species, self.move)
        result["version_group_details"] = from_list(lambda x: to_class(VersionGroupDetail, x), self.version_group_details)
        return result


@dataclass
class RedBlue:
    back_default: str
    back_gray: str
    front_default: str
    front_gray: str

    @staticmethod
    def from_dict(obj: Any) -> 'RedBlue':
        assert isinstance(obj, dict)
        back_default = from_str(obj.get("back_default"))
        back_gray = from_str(obj.get("back_gray"))
        front_default = from_str(obj.get("front_default"))
        front_gray = from_str(obj.get("front_gray"))
        return RedBlue(back_default, back_gray, front_default, front_gray)

    def to_dict(self) -> dict:
        result: dict = {}
        result["back_default"] = from_str(self.back_default)
        result["back_gray"] = from_str(self.back_gray)
        result["front_default"] = from_str(self.front_default)
        result["front_gray"] = from_str(self.front_gray)
        return result


@dataclass
class GenerationI:
    red_blue: RedBlue
    yellow: RedBlue

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationI':
        assert isinstance(obj, dict)
        red_blue = RedBlue.from_dict(obj.get("red-blue"))
        yellow = RedBlue.from_dict(obj.get("yellow"))
        return GenerationI(red_blue, yellow)

    def to_dict(self) -> dict:
        result: dict = {}
        result["red-blue"] = to_class(RedBlue, self.red_blue)
        result["yellow"] = to_class(RedBlue, self.yellow)
        return result


@dataclass
class Crystal:
    back_default: str
    back_shiny: str
    front_default: str
    front_shiny: str

    @staticmethod
    def from_dict(obj: Any) -> 'Crystal':
        assert isinstance(obj, dict)
        back_default = from_str(obj.get("back_default"))
        back_shiny = from_str(obj.get("back_shiny"))
        front_default = from_str(obj.get("front_default"))
        front_shiny = from_str(obj.get("front_shiny"))
        return Crystal(back_default, back_shiny, front_default, front_shiny)

    def to_dict(self) -> dict:
        result: dict = {}
        result["back_default"] = from_str(self.back_default)
        result["back_shiny"] = from_str(self.back_shiny)
        result["front_default"] = from_str(self.front_default)
        result["front_shiny"] = from_str(self.front_shiny)
        return result


@dataclass
class GenerationIi:
    crystal: Crystal
    gold: Crystal
    silver: Crystal

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationIi':
        assert isinstance(obj, dict)
        crystal = Crystal.from_dict(obj.get("crystal"))
        gold = Crystal.from_dict(obj.get("gold"))
        silver = Crystal.from_dict(obj.get("silver"))
        return GenerationIi(crystal, gold, silver)

    def to_dict(self) -> dict:
        result: dict = {}
        result["crystal"] = to_class(Crystal, self.crystal)
        result["gold"] = to_class(Crystal, self.gold)
        result["silver"] = to_class(Crystal, self.silver)
        return result


@dataclass
class Emerald:
    front_default: str
    front_shiny: str

    @staticmethod
    def from_dict(obj: Any) -> 'Emerald':
        assert isinstance(obj, dict)
        front_default = from_str(obj.get("front_default"))
        front_shiny = from_str(obj.get("front_shiny"))
        return Emerald(front_default, front_shiny)

    def to_dict(self) -> dict:
        result: dict = {}
        result["front_default"] = from_str(self.front_default)
        result["front_shiny"] = from_str(self.front_shiny)
        return result


@dataclass
class GenerationIii:
    emerald: Emerald
    firered_leafgreen: Crystal
    ruby_sapphire: Crystal

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationIii':
        assert isinstance(obj, dict)
        emerald = Emerald.from_dict(obj.get("emerald"))
        firered_leafgreen = Crystal.from_dict(obj.get("firered-leafgreen"))
        ruby_sapphire = Crystal.from_dict(obj.get("ruby-sapphire"))
        return GenerationIii(emerald, firered_leafgreen, ruby_sapphire)

    def to_dict(self) -> dict:
        result: dict = {}
        result["emerald"] = to_class(Emerald, self.emerald)
        result["firered-leafgreen"] = to_class(Crystal, self.firered_leafgreen)
        result["ruby-sapphire"] = to_class(Crystal, self.ruby_sapphire)
        return result


@dataclass
class Home:
    front_default: str
    front_female: None
    front_shiny: str
    front_shiny_female: None

    @staticmethod
    def from_dict(obj: Any) -> 'Home':
        assert isinstance(obj, dict)
        front_default = from_str(obj.get("front_default"))
        front_female = from_none(obj.get("front_female"))
        front_shiny = from_str(obj.get("front_shiny"))
        front_shiny_female = from_none(obj.get("front_shiny_female"))
        return Home(front_default, front_female, front_shiny, front_shiny_female)

    def to_dict(self) -> dict:
        result: dict = {}
        result["front_default"] = from_str(self.front_default)
        result["front_female"] = from_none(self.front_female)
        result["front_shiny"] = from_str(self.front_shiny)
        result["front_shiny_female"] = from_none(self.front_shiny_female)
        return result


@dataclass
class DreamWorld:
    front_default: str
    front_female: None

    @staticmethod
    def from_dict(obj: Any) -> 'DreamWorld':
        assert isinstance(obj, dict)
        front_default = from_str(obj.get("front_default"))
        front_female = from_none(obj.get("front_female"))
        return DreamWorld(front_default, front_female)

    def to_dict(self) -> dict:
        result: dict = {}
        result["front_default"] = from_str(self.front_default)
        result["front_female"] = from_none(self.front_female)
        return result


@dataclass
class GenerationVii:
    icons: DreamWorld
    ultra_sun_ultra_moon: Home

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationVii':
        assert isinstance(obj, dict)
        icons = DreamWorld.from_dict(obj.get("icons"))
        ultra_sun_ultra_moon = Home.from_dict(obj.get("ultra-sun-ultra-moon"))
        return GenerationVii(icons, ultra_sun_ultra_moon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["icons"] = to_class(DreamWorld, self.icons)
        result["ultra-sun-ultra-moon"] = to_class(Home, self.ultra_sun_ultra_moon)
        return result


@dataclass
class GenerationViii:
    icons: DreamWorld

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationViii':
        assert isinstance(obj, dict)
        icons = DreamWorld.from_dict(obj.get("icons"))
        return GenerationViii(icons)

    def to_dict(self) -> dict:
        result: dict = {}
        result["icons"] = to_class(DreamWorld, self.icons)
        return result


@dataclass
class OfficialArtwork:
    front_default: str

    @staticmethod
    def from_dict(obj: Any) -> 'OfficialArtwork':
        assert isinstance(obj, dict)
        front_default = from_str(obj.get("front_default"))
        return OfficialArtwork(front_default)

    def to_dict(self) -> dict:
        result: dict = {}
        result["front_default"] = from_str(self.front_default)
        return result


@dataclass
class Other:
    dream_world: DreamWorld
    home: Home
    official_artwork: OfficialArtwork

    @staticmethod
    def from_dict(obj: Any) -> 'Other':
        assert isinstance(obj, dict)
        dream_world = DreamWorld.from_dict(obj.get("dream_world"))
        home = Home.from_dict(obj.get("home"))
        official_artwork = OfficialArtwork.from_dict(obj.get("official-artwork"))
        return Other(dream_world, home, official_artwork)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dream_world"] = to_class(DreamWorld, self.dream_world)
        result["home"] = to_class(Home, self.home)
        result["official-artwork"] = to_class(OfficialArtwork, self.official_artwork)
        return result


@dataclass
class GenerationV:
    black_white: 'Sprites'

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationV':
        assert isinstance(obj, dict)
        black_white = Sprites.from_dict(obj.get("black-white"))
        return GenerationV(black_white)

    def to_dict(self) -> dict:
        result: dict = {}
        result["black-white"] = to_class(Sprites, self.black_white)
        return result


@dataclass
class GenerationIv:
    diamond_pearl: 'Sprites'
    heartgold_soulsilver: 'Sprites'
    platinum: 'Sprites'

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationIv':
        assert isinstance(obj, dict)
        diamond_pearl = Sprites.from_dict(obj.get("diamond-pearl"))
        heartgold_soulsilver = Sprites.from_dict(obj.get("heartgold-soulsilver"))
        platinum = Sprites.from_dict(obj.get("platinum"))
        return GenerationIv(diamond_pearl, heartgold_soulsilver, platinum)

    def to_dict(self) -> dict:
        result: dict = {}
        result["diamond-pearl"] = to_class(Sprites, self.diamond_pearl)
        result["heartgold-soulsilver"] = to_class(Sprites, self.heartgold_soulsilver)
        result["platinum"] = to_class(Sprites, self.platinum)
        return result


@dataclass
class Versions:
    generation_i: GenerationI
    generation_ii: GenerationIi
    generation_iii: GenerationIii
    generation_iv: GenerationIv
    generation_v: GenerationV
    generation_vi: Dict[str, Home]
    generation_vii: GenerationVii
    generation_viii: GenerationViii

    @staticmethod
    def from_dict(obj: Any) -> 'Versions':
        assert isinstance(obj, dict)
        generation_i = GenerationI.from_dict(obj.get("generation-i"))
        generation_ii = GenerationIi.from_dict(obj.get("generation-ii"))
        generation_iii = GenerationIii.from_dict(obj.get("generation-iii"))
        generation_iv = GenerationIv.from_dict(obj.get("generation-iv"))
        generation_v = GenerationV.from_dict(obj.get("generation-v"))
        generation_vi = from_dict(Home.from_dict, obj.get("generation-vi"))
        generation_vii = GenerationVii.from_dict(obj.get("generation-vii"))
        generation_viii = GenerationViii.from_dict(obj.get("generation-viii"))
        return Versions(generation_i, generation_ii, generation_iii, generation_iv, generation_v, generation_vi, generation_vii, generation_viii)

    def to_dict(self) -> dict:
        result: dict = {}
        result["generation-i"] = to_class(GenerationI, self.generation_i)
        result["generation-ii"] = to_class(GenerationIi, self.generation_ii)
        result["generation-iii"] = to_class(GenerationIii, self.generation_iii)
        result["generation-iv"] = to_class(GenerationIv, self.generation_iv)
        result["generation-v"] = to_class(GenerationV, self.generation_v)
        result["generation-vi"] = from_dict(lambda x: to_class(Home, x), self.generation_vi)
        result["generation-vii"] = to_class(GenerationVii, self.generation_vii)
        result["generation-viii"] = to_class(GenerationViii, self.generation_viii)
        return result


@dataclass
class Sprites:
    back_default: str
    back_female: None
    back_shiny: str
    back_shiny_female: None
    front_default: str
    front_female: None
    front_shiny: str
    front_shiny_female: None
    other: Optional[Other] = None
    versions: Optional[Versions] = None
    animated: Optional['Sprites'] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Sprites':
        assert isinstance(obj, dict)
        back_default = from_str(obj.get("back_default"))
        back_female = from_none(obj.get("back_female"))
        back_shiny = from_str(obj.get("back_shiny"))
        back_shiny_female = from_none(obj.get("back_shiny_female"))
        front_default = from_str(obj.get("front_default"))
        front_female = from_none(obj.get("front_female"))
        front_shiny = from_str(obj.get("front_shiny"))
        front_shiny_female = from_none(obj.get("front_shiny_female"))
        other = from_union([Other.from_dict, from_none], obj.get("other"))
        versions = from_union([Versions.from_dict, from_none], obj.get("versions"))
        animated = from_union([Sprites.from_dict, from_none], obj.get("animated"))
        return Sprites(back_default, back_female, back_shiny, back_shiny_female, front_default, front_female, front_shiny, front_shiny_female, other, versions, animated)

    def to_dict(self) -> dict:
        result: dict = {}
        result["back_default"] = from_str(self.back_default)
        result["back_female"] = from_none(self.back_female)
        result["back_shiny"] = from_str(self.back_shiny)
        result["back_shiny_female"] = from_none(self.back_shiny_female)
        result["front_default"] = from_str(self.front_default)
        result["front_female"] = from_none(self.front_female)
        result["front_shiny"] = from_str(self.front_shiny)
        result["front_shiny_female"] = from_none(self.front_shiny_female)
        result["other"] = from_union([lambda x: to_class(Other, x), from_none], self.other)
        result["versions"] = from_union([lambda x: to_class(Versions, x), from_none], self.versions)
        result["animated"] = from_union([lambda x: to_class(Sprites, x), from_none], self.animated)
        return result


@dataclass
class Stat:
    base_stat: int
    effort: int
    stat: Species

    @staticmethod
    def from_dict(obj: Any) -> 'Stat':
        assert isinstance(obj, dict)
        base_stat = from_int(obj.get("base_stat"))
        effort = from_int(obj.get("effort"))
        stat = Species.from_dict(obj.get("stat"))
        return Stat(base_stat, effort, stat)

    def to_dict(self) -> dict:
        result: dict = {}
        result["base_stat"] = from_int(self.base_stat)
        result["effort"] = from_int(self.effort)
        result["stat"] = to_class(Species, self.stat)
        return result


@dataclass
class TypeElement:
    slot: int
    type: Species

    @staticmethod
    def from_dict(obj: Any) -> 'TypeElement':
        assert isinstance(obj, dict)
        slot = from_int(obj.get("slot"))
        type = Species.from_dict(obj.get("type"))
        return TypeElement(slot, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["slot"] = from_int(self.slot)
        result["type"] = to_class(Species, self.type)
        return result


@dataclass
class Pokedex:
    abilities: List[Ability]
    base_experience: int
    forms: List[Species]
    game_indices: List[GameIndex]
    height: int
    held_items: List[Any]
    id: int
    is_default: bool
    location_area_encounters: str
    moves: List[Move]
    name: str
    order: int
    past_types: List[Any]
    species: Species
    sprites: Sprites
    stats: List[Stat]
    types: List[TypeElement]
    weight: int

    @staticmethod
    def from_dict(obj: Any) -> 'Pokedex':
        assert isinstance(obj, dict)
        abilities = from_list(Ability.from_dict, obj.get("abilities"))
        base_experience = from_int(obj.get("base_experience"))
        forms = from_list(Species.from_dict, obj.get("forms"))
        game_indices = from_list(GameIndex.from_dict, obj.get("game_indices"))
        height = from_int(obj.get("height"))
        held_items = from_list(lambda x: x, obj.get("held_items"))
        id = from_int(obj.get("id"))
        is_default = from_bool(obj.get("is_default"))
        location_area_encounters = from_str(obj.get("location_area_encounters"))
        moves = from_list(Move.from_dict, obj.get("moves"))
        name = from_str(obj.get("name"))
        order = from_int(obj.get("order"))
        past_types = from_list(lambda x: x, obj.get("past_types"))
        species = Species.from_dict(obj.get("species"))
        sprites = Sprites.from_dict(obj.get("sprites"))
        stats = from_list(Stat.from_dict, obj.get("stats"))
        types = from_list(TypeElement.from_dict, obj.get("types"))
        weight = from_int(obj.get("weight"))
        return Pokedex(abilities, base_experience, forms, game_indices, height, held_items, id, is_default, location_area_encounters, moves, name, order, past_types, species, sprites, stats, types, weight)

    def to_dict(self) -> dict:
        result: dict = {}
        result["abilities"] = from_list(lambda x: to_class(Ability, x), self.abilities)
        result["base_experience"] = from_int(self.base_experience)
        result["forms"] = from_list(lambda x: to_class(Species, x), self.forms)
        result["game_indices"] = from_list(lambda x: to_class(GameIndex, x), self.game_indices)
        result["height"] = from_int(self.height)
        result["held_items"] = from_list(lambda x: x, self.held_items)
        result["id"] = from_int(self.id)
        result["is_default"] = from_bool(self.is_default)
        result["location_area_encounters"] = from_str(self.location_area_encounters)
        result["moves"] = from_list(lambda x: to_class(Move, x), self.moves)
        result["name"] = from_str(self.name)
        result["order"] = from_int(self.order)
        result["past_types"] = from_list(lambda x: x, self.past_types)
        result["species"] = to_class(Species, self.species)
        result["sprites"] = to_class(Sprites, self.sprites)
        result["stats"] = from_list(lambda x: to_class(Stat, x), self.stats)
        result["types"] = from_list(lambda x: to_class(TypeElement, x), self.types)
        result["weight"] = from_int(self.weight)
        return result


def pokedex_from_dict(s: Any) -> Pokedex:
    return Pokedex.from_dict(s)


def pokedex_to_dict(x: Pokedex) -> Any:
    return to_class(Pokedex, x)
