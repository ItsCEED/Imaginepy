from enum import Enum

# Banned
BANNED_WORDS = ['xxx']


# KEY = (parameter, images, thumbnail)
class Mode(Enum):
    SCRIBBLE = ('scribble', 'assets/imageRemix_modes/scribble.webp',
                'assets/imageRemix_modes/thumb_scribble.webp')
    DEPTH = ('depth', 'assets/imageRemix_modes/depth.webp',
             'assets/imageRemix_modes/thumb_depth.webp')
    OPEN_POSE = ('openpose', 'assets/imageRemix_modes/openpose.webp',
                 'assets/imageRemix_modes/thumb_openpose.webp')
    LINE_ART = ('lineart', 'assets/imageRemix_modes/lineartanime.webp',
                'assets/imageRemix_modes/thumb_lineartanime.webp')
    CANNY = ('canny', 'assets/imageRemix_modes/canny.webp',
             'assets/imageRemix_modes/thumb_canny.webp')


# KEY = ratio
class Ratio(Enum):
    RATIO_1X1 = "1:1"
    RATIO_4X3 = "4:3"
    RATIO_3X2 = "3:2"
    RATIO_2X3 = "2:3"
    RATIO_16X9 = "16:9"
    RATIO_9X16 = "9:16"
    RATIO_5X4 = "5:4"
    RATIO_4X5 = "4:5"
    RATIO_3X1 = "3:1"
    RATIO_3X4 = "3:4"


# KEY = (model_id, name, thumb)
class Model(Enum):
    V4_BETA = (30, ' V4(Beta)', 'assets/styles_v1/Imagine_V3.5.webp')
    CREATIVE = (31, 'Creative', 'assets/styles_v4/thumb-73.webp')
    V3 = (28, 'V3', 'assets/styles_v4/thumb-74.webp', ', 4k, high quality, hdr')
    V1 = (27, 'V1', 'assets/styles_v4/thumb-63.webp')
    PORTRAIT = (26, 'Portrait', 'assets/styles_v4/thumb-65.webp')
    REALISTIC = (29, 'Realistic', 'assets/styles_v4/thumb-72.webp')
    ANIME = (21, 'Anime', 'assets/styles/thumb_20.webp')


# KEY = (style_id, style_name, style_thumb, init_prompt)
class Style(Enum):
    NO_STYLE = (27, 'No style', '', '')
    EUPHORIC = (28, 'Euphoric', 'assets/styles_v4/thumb-20.webp',
                'digital illustration, style of charlie bowater, dreamy colorful cyberpunk colors, euphoric fantasy, epic dreamlike fantasy landscape, beautiful oil matte painting, 8k fantasy art, fantasy art landscape, jessica rossier color scheme, dreamlike diffusion')
    FANTASY = (28, 'Fantasy', 'assets/styles_v4/thumb-25.webp',
               'fantasy matte painting,  fantasy landscape, ( ( thomas kinkade ) ), whimsical, dreamy, alice in wonderland, daydreaming, epic scene, high exposure, highly detailed, tim white, michael whelan')
    CYBERPUNK = (28, 'Cyberpunk', 'assets/styles_v1/thumb_41.webp',
                 ', synthwave image, (neotokyo), dreamy colorful cyberpunk colors, cyberpunk blade runner art, retrofuturism, cyberpunk, beautiful cyberpunk style, cgsociety 9')
    STUDIO_GHIBLI = (28, 'Studio Ghibli', 'assets/styles_v4/thumb-07.webp',
                     'studio ghibli movie still, ghibli screenshot, joe hisaishi, makoto shinkai, cinematic studio ghibli still, fantasy art landscape, whimsical, dreamlike, anime beautiful peace scene, studio ghibli painting, cinematic')
    DISNEY = (28, 'Disney', 'assets/styles_v4/thumb-04.webp',
              'disney animation, disney splash art, disney color palette, disney renaissance film, disney pixar movie still, disney art style, disney concept art :: nixri, wonderful compositions, pixar, disney concept artists, 2d character design')
    GTA = (28, 'GTA', 'assets/styles_v4/thumb-06.webp',
           'gta iv art style, gta art,  gta loading screen art, gta chinatowon art style, gta 5 loading screen poster, grand theft auto 5, grand theft auto video game')
    KAWAII_CHIBI = (28, 'Kawaii Chibi', 'assets/styles_v4/thumb-40.webp',
                    'kawaii chibi romance, fantasy, illustration, Colorful idyllic cheerful, Kawaii Chibi inspired')
    ANIME_V2 = (28, 'Anime V2', 'assets/styles_v1/thumb_37.webp', ', anime atmospheric, atmospheric anime, anime character; full body art, digital anime art, beautiful anime art style, anime picture, anime arts, beautiful anime style, digital advanced anime art, anime painting, anime artwork, beautiful anime art, detailed digital anime art, anime epic artwork')
    ABSTRACT_VIBRANT = (28, 'Abstract Vibrant', 'assets/styles_v4/thumb-31.webp',
                        'vibrant, editorial, abstract elements, colorful, color splatter, realism, Inspired by the style of Ryan Hewett, dynamic realism, soft lighting and intricate details')
    VIBRANT = (27, 'Vibrant', 'assets/styles_v4/thumb-62.webp',
               ', Psychedelic, water colors spots, vibrant color scheme, highly detailed, romanticism style, cinematic, artstation, greg rutkowski')
    PSYCHEDELIC = (28, 'Psychedelic', 'assets/styles_v4/thumb-11.webp',
                   'psychedelic painting, psychedelic dripping colors, colorful detailed projections, android jones and chris dyer, psychedelic vibrant colors, intricate psychedelic patterns, psychedelic visuals, hallucinatory art')
    EXTRA_TERRESTRIAL = (28, 'Extra-terrestrial', 'assets/styles_v4/thumb-26.webp',
                         'deepdream cosmic, painting by android jones, cosmic entity, humanoid creature, james jean soft light 4 k, sci fi, extra terrestrial, cinematic')
    COSMIC = (28, 'Cosmic', 'assets/styles_v4/thumb-01.webp',
              'in cosmic atmosphere, humanitys cosmic future,  space art concept, space landscape, scene in space, cosmic space, beautiful space star planet, background in space, realistic, cinematic, breathtaking view')
    MACRO_PHOTOGRAPHY = (28, 'Macro Photography', 'assets/styles_v4/thumb-05.webp',
                         'macro photography, award winning macro photography, depth of field, extreme closeup, 8k hd, focused')
    PRODUCT_PHOTOGRAPHY = (28, 'Product Photography', 'assets/styles_v4/thumb-10.webp',
                           'product photo studio lighting,  high detail product photo, product photography, commercial product photography, realistic, light, 8k, award winning product photography, professional closeup')
    POLAROID = (27, 'Polaroid', 'assets/styles_v4/thumb-54.webp',
                ', old polaroid, 35mm')
    NEO_FAUVISM = (28, 'Neo fauvism', 'assets/styles_v4/thumb-28.webp',
                   'neo-fauvism painting, neo-fauvism movement, digital illustration, poster art, cgsociety saturated colors, fauvist')
    POP_ART = (28, 'Pop Art', 'assets/styles_v4/thumb-23.webp',
               'pop art painting, detailed patterns pop art, silkscreen pop art, pop art poster, roy lichtenstein style')
    POP_ART_II = (28, 'Pop Art II', 'assets/styles_v4/thumb-70.webp',
                  'style of shepherd fairey, (Andy Warhol art style), silkscreen pop art, martin ansin artwork, high contrast illustrations, lowbrow pop art style, trending on artstatioin, vector style')
    GRAFFITI = (28, 'Graffiti', 'assets/styles_v4/thumb-13.webp',
                'graffiti background, colorful graffiti, graffiti art style, colorful mural, ravi supa, symbolic mural, juxtapoz, pablo picasso, street art')
    SURREALISM = (28, 'Surrealism', 'assets/styles_v4/thumb-12.webp',
                  'salvador dali painting, highly detailed surrealist art, surrealist conceptual art,  masterpiece surrealism, surreal architecture, surrealistic digital artwork, whimsical surrealism, bizarre art')
    BAUHAUS = (28, 'Bauhaus', 'assets/styles_v4/thumb-34.webp',
               'Bauhaus art movement,  by Wassily Kandinsky, bauhaus style painting, geometric abstraction, vibrant colors, painting')
    CUBISM = (28, 'Cubism', 'assets/styles_v4/thumb-33.webp',
              'cubist picasso, cubism,  a cubist painting, heavy cubism, cubist painting, by Carlo Carrà, style of picasso, modern cubism, futuristic cubism')
    JAPANESE_ART = (27, 'Japanese Art', 'assets/styles_v4/thumb-51.webp',
                    ', Ukiyoe, illustration, muted colors')
    SKETCH = (27, 'Sketch', 'assets/styles_v4/thumb-59.webp',
              ', pencil, hand drawn, sketch, on paper')
    ILLUSTRATION = (28, 'Illustration', 'assets/styles_v1/thumb_31.webp',
                    ', minimalistic vector art, illustrative style, style of ian hubert, style of gilles beloeil, inspired by Hsiao-Ron Cheng, style of jonathan solter, style of alexandre chaudret, by Echo Chernik')
    PAINTING = (28, 'Painting', 'assets/styles_v1/thumb_32.webp',
                ', atmospheric dreamscape painting, by Mac Conner, vibrant gouache painting scenery, vibrant painting, vivid painting, a beautiful painting, dream scenery art, instagram art, psychedelic painting, lofi art, bright art')
    PALETTE_KNIFE = (28, 'Palette Knife', 'assets/styles_v4/thumb-17.webp',
                     'detailed impasto brush strokes,  detail acrylic palette knife, thick impasto technique,  palette knife, vibrant 8k colors')
    INK = (27, 'Ink', 'assets/styles_v4/thumb-50.webp',
           ', Black Ink, Hand drawn, Minimal art, artstation, artgem, monochrome')
    ORIGAMI = (28, 'Origami', 'assets/styles_v4/thumb-22.webp',
               'polygonal art, layered paper art, paper origami, wonderful compositions, folded geometry, paper craft, made from paper')
    STAINED_GLASS = (28, 'Stained Glass', 'assets/styles_v4/thumb-09.webp',
                     'intricate wiccan spectrum, stained glass art, vividly beautiful colors, beautiful stained glass window, colorful image, intricate stained glass triptych, gothic stained glass style, stained glass window!!!')
    STICKER = (28, 'Sticker', 'assets/styles_v1/thumb_35.webp',
               ', sticker, sticker art, symmetrical sticker design, sticker - art, sticker illustration, die - cut sticker')
    CLIP_ART = (28, 'Clip Art', 'assets/styles_v4/thumb-69.webp',
                '(((clip art))), clip art illustration, cartoon character, thin black stroke outline, pastel colors, cute illustration,  vector illustration')
    POSTER_ART = (27, 'Poster Art', 'assets/styles_v4/thumb-56.webp',
                  ', album art, Poster, layout, typography, logo, risography, ghibili, simon stalenhag, insane detail, artstation, 8k')
    PAPERCUT_STYLE = (28, 'PaperCut Style', 'assets/styles_v1/thumb_39.webp',
                      ', layered paper art, paper modeling art, paper craft, paper art, papercraft, paper cutout, paper cut out collage artwork, paper cut art')
    COLORING_BOOK = (28, 'Coloring Book', 'assets/styles_v4/thumb-67.webp',
                     ', line art illustration, lineart behance hd, illustration line art style, line art colouring page, decora inspired illustrations, coloring pages, digital line-art, line art!!, thick line art, coloring book page, clean coloring book page, black ink line art, coloring page, detailed line art')
    PATTERN = (28, 'Pattern', 'assets/styles_v4/thumb-71.webp',
               'seamless pattern, ((repetitive pattern)), pattern design, background image, wallpaper,  colorful, decorated, flat design')
    RENDER = (28, 'Render', 'assets/styles_v1/thumb_36.webp',
              ', isometric, polaroid octane render, 3 d render 1 5 0 mm lens, keyshot product render, rendered, keyshot product render pinterest, 3 d product render, 3 d cgi render, 3d cgi render, ultra wide angle isometric view')
    CINEMATIC_RENDER = (27, 'Cinematic Render', 'assets/styles_v4/thumb-47.webp',
                        ', cinematic, breathtaking colors, close-up, cgscociety, computer rendering, by mike winkelmann, uhd, rendered in cinema4d, surface modeling, 8k, render octane, inspired by beksinski')
    COMIC_BOOK = (28, 'Comic Book', 'assets/styles_v4/thumb-48.webp',
                  ', Comic cover, 1960s marvel comic, comic book illustrations')
    COMIC_V2 = (28, 'Comic V2', 'assets/styles_v1/thumb_34.webp',
                ', comic book, john romita senior, inspired by Alton Tobey, by Alan Davis, arachnophobia, by Alton Tobey, as a panel of a marvel comic, marvel comic')
    LOGO = (28, 'Logo', 'assets/styles_v4/thumb-37.webp',
            'creative logo, unique logo, visual identity, geometric type, graphic design, logotype design, brand identity, vector based, trendy typography, best of behance')
    ICON = (28, 'Icon', 'assets/styles_v1/thumb_43.webp',
            ', single vector graphics icon, ios icon, smooth shape, vector')
    GLASS_ART = (28, 'Glass Art', 'assets/styles_v1/thumb_46.webp',
                 ' inside glass ball, translucent sphere, cgsociety 9, glass orb, behance, polished, beautiful digital artwork, exquisite digital art, in a short round glass vase, octane render')
    KNOLLING_CASE = (28, 'Knolling Case', 'assets/styles_v1/thumb_45.webp',
                     ', in  square glass case,  glass cube, glowing, knolling case, ash thorp, studio background,  desktopography, cgsociety 9,  cgsociety, mind-bending digital art')
    SCATTER = (28, 'Scatter', 'assets/styles_v1/thumb_42.webp',
               ', breaking pieces, exploding pieces, shattering pieces,  disintegration, contemporary digital art, inspired by Dan Hillier, inspired by Igor Morski, dramatic digital art, behance art, cgsociety 9, 3d advanced digital art, mind-bending digital art, disintegrating')
    POLY_ART = (27, 'Poly Art', 'assets/styles_v4/thumb-55.webp',
                ', low poly, artstation, studio lightning, stainless steel, grey color scheme')
    CLAYMATION = (28, 'Claymation', 'assets/styles_v4/thumb-19.webp',
                  'clay animation, as a claymation character, claymation style, animation key shot, plasticine, clay animation, stopmotion animation, aardman character design, plasticine models')
    WOOLITIZE = (28, 'Woolitize', 'assets/styles_v4/thumb-27.webp',
                 'cute! c4d, made out of wool, volumetric wool felting, wool felting art, houdini sidefx, rendered in arnold, soft smooth lighting, soft pastel colors')
    MARBLE = (28, 'Marble', 'assets/styles_v4/thumb-02.webp',
              'in greek marble style, classical antiquities, ancient greek classical ancient greek art, marble art, realistic, cinematic')
    VAN_GOGH = (27, 'Van Gogh', 'assets/styles_v4/thumb-61.webp',
                ', painting, by van gogh')
    SALVADOR_DALI = (27, 'Salvador Dali', 'assets/styles_v4/thumb-58.webp',
                     ', Painting, by salvador dali, allegory, surrealism, religious art, genre painting, portrait, painter, still life')
    PICASSO = (27, 'Picasso', 'assets/styles_v4/thumb-53.webp',
               ', painting, by pablo picaso, cubism')
    ARCHITECTURE = (28, 'Architecture', 'assets/styles_v1/thumb_47.webp',
                    ', modern architecture design, luxury architecture, bright, very beautiful, trending on unsplash, breath taking')
    INTERIOR = (28, 'Interior', 'assets/styles_v1/thumb_40.webp',
                ', modern architecture by makoto shinkai, ilya kuvshinov, lois van baarle, rossdraws and frank lloyd wright')
    ABSTRACT_CITYSCAPE = (28, 'Abstract Cityscape', 'assets/styles_v4/thumb-46.webp',
                          'abstract cityscape, Ultra Realistic Cinematic Light abstract, futuristic, cityscape, Out of focus background and incredible 16k resolution produced in Unreal Engine 5 and Octan render')
    DYSTOPIAN = (28, 'Dystopian', 'assets/styles_v4/thumb-08.webp',
                 'cifi world, cybernetic civilizations, peter gric and dan mumford,   brutalist dark futuristic, dystopian brutalist atmosphere, dark dystopian world, cinematic 8k, end of the world, doomsday')
    FUTURISTIC = (27, 'Futuristic', 'assets/styles_v4/thumb-49.webp',
                  ', futuristic, elegant atmosphere, glowing lights, highly detailed, digital painting, artstation, concept art, smooth sharp focus, illustration, mars ravelo, gereg rutkowski')
    NEON = (28, 'Neon', 'assets/styles_v4/thumb-32.webp',
            'neon art style, night time dark with neon colors, blue neon lighting, violet and aqua neon lights, blacklight neon colors, rococo cyber neon lighting')
    CHROMATIC = (28, 'Chromatic', 'assets/styles_v4/thumb-68.webp',
                 '(((chromatic))) vaporwave nostalgia, vaporwave artwork, ((synthwave)), chromatic colors, , 3d render, vibrant chromatic colors, glowing chromatic colors')
    MYSTICAL = (27, 'Mystical', 'assets/styles_v4/thumb-52.webp',
                ', fireflies, deep focus, d&d, fantasy, intricate, elegant, highly detailed, digital painting, artstation, concept art, matte, sharp focus, illustration, hearthstrom, gereg rutkowski, alphonse mucha, andreas rocha')
    LANDSCAPE = (28, 'Landscape', 'assets/styles_v1/thumb_44.webp',
                 ', landscape 4k, beautiful landscapes, nature wallpaper, 8k photography')
    RAINBOW = (28, 'Rainbow', 'assets/styles_v4/thumb-15.webp',
               'intricate rainbow environment, rainbow bg, from lorax movie, pixar color palette, volumetric rainbow lighting, gorgeous digital painting, 8k cinematic')
    CANDYLAND = (28, 'Candyland', 'assets/styles_v4/thumb-18.webp',
                 'candy land style,  whimsical fantasy landscape art, japanese pop surrealism, colorfull digital fantasy art, made of candy and lollypops, whimsical and dreamy')
    MINECRAFT = (28, 'Minecraft', 'assets/styles_v4/thumb-03.webp',
                 'minecraft build, style of minecraft, pixel style, 8 bit, epic, cinematic, screenshot from minecraft, detailed natural lighting, minecraft gameplay, mojang,  minecraft mods, minecraft in real life,  blocky like minecraft')
    PIXEL_ART = (28, 'Pixel Art', 'assets/styles_v1/thumb_38.webp',
                 ', one pixel brush, pixelart, colorful pixel art')
    RENNAISANCE = (28, 'Rennaisance', 'assets/styles_v4/thumb-24.webp',
                   'renaissance period, neo-classical painting, italian renaissance workshop, pittura metafisica, raphael high renaissance, ancient roman painting, michelangelo painting, Leonardo da Vinci, italian renaissance architecture')
    ROCOCCO = (28, 'Rococco', 'assets/styles_v4/thumb-35.webp',
               'francois boucher oil painting, rococco style,  rococco lifestyle, a flemish Baroque, by Karel Dujardin, vintage look, cinematic hazy lighting')
    MEDIEVAL = (28, 'Medieval', 'assets/styles_v4/thumb-21.webp',
                'movie still from game of thrones, powerful fantasy epic, middle ages, lush green landscape, olden times, roman empire, 1400 ce, highly detailed background, cinematic lighting, 8k render, high quality, bright colours')
    RETRO = (28, 'Retro', 'assets/styles_v1/thumb_30.webp', ', retro futuristic illustration, featured on illustrationx, art deco illustration, beautiful retro art, stylized digital illustration, highly detailed vector art, ( ( mads berg ) ), automotive design art, epic smooth illustration, by mads berg, stylized illustration, ash thorp khyzyl saleem, clean vector art')
    RETROWAVE = (27, 'Retrowave', 'assets/styles_v4/thumb-57.webp',
                 ', Illustration, retrowave art, noen light, retro, digital art, trending on artstation')
    STEAMPUNK = (27, 'Steampunk', 'assets/styles_v4/thumb-60.webp',
                 ' steampunk, stylized digital illustration, sharp focus, elegant, intricate, digital painting, artstation concept art, global illumination, ray tracing, advanced technology, chaykan howard, campion pascal, cooke darwin, davis jack, pink atmosphere')
    AMAZONIAN = (28, 'Amazonian', 'assets/styles_v4/thumb-29.webp',
                 'amazonian cave, landscape, jungle, waterfall, moss-covered ancient ruins, Dramatic lighting and intense colors, mesmerizing details of the environment and breathtaking atmosphere')
    AVATAR = (28, 'Avatar', 'assets/styles_v4/thumb-16.webp',
              'avatar movie, avatar with blue skin, vfx movie, cinematic lighting, utopian jungle, pandora jungle, sci-fi nether world, lost world, pandora fantasy landscape,lush green landscape, high quality render')
    GOTHIC = (28, 'Gothic', 'assets/styles_v4/thumb-14.webp',
              'goth lifestyle, dark goth, grunge, cinematic photography, dramatic dark scenery, dark ambient beautiful')
    HAUNTED = (28, 'Haunted', 'assets/styles_v4/thumb-36.webp',
               'horror cgi 4 k, scary color art in 4 k, horror movie cinematography, insidious, la llorona, still from animated horror movie, film still from horror movie, haunted, eerie, unsettling, creepy')
    WATERBENDER = (28, 'Waterbender', 'assets/styles_v4/thumb-38.webp',
                   'water elements, fantasy, water, exotic, A majestic composition with water elements, waterfall, lush moss and exotic flowers, highly detailed and realistic, dynamic lighting')
    AQUATIC = (28, 'Aquatic', 'assets/styles_v4/thumb-44.webp',
               'graceful movement with intricate details, inspired by artists like Lotte Reiniger, Carne Griffiths and Alphonse Mucha. Dreamy and surreal atmosphere, twirling in an aquatic landscape with water surface')
    FIREBENDER = (28, 'Firebender', 'assets/styles_v4/thumb-39.webp',
                  'fire elements, fantasy, fire, lava, striking. A majestic composition with fire elements, fire and ashes surrounding, highly detailed and realistic, cinematic lighting')
    FORESTPUNK = (28, 'Forestpunk', 'assets/styles_v4/thumb-41.webp',
                  'forestpunk, vibrant, HDRI, organic motifs and pollen in the air, bold vibrant colors and textures, spectacular sparkling rays, photorealistic quality with Hasselblad')
    VIBRANT_VIKING = (28, 'Vibrant Viking', 'assets/styles_v4/thumb-45.webp',
                      'Viking era, digital painting, pop of colour, forest, paint splatter, flowing colors, Background of lush forest and earthy tones, Artistic representation of movement and atmosphere')
    SAMURAI = (28, 'Samurai', 'assets/styles_v4/thumb-43.webp',
               'samurai lifesyle, miyamoto musashi, Japanese art, ancient japanese samurai, feudal japan art, feudal japan art')
    ELVEN = (28, 'Elven', 'assets/styles_v4/thumb-42.webp',
             'elven lifestyle, photoreal, realistic, 32k quality, crafted by Elves and engraved in copper, elven fantasy land, hyper detailed')
    SHAMROCK_FANTASY = (28, 'Shamrock Fantasy', 'assets/styles_v4/thumb-30.webp',
                        'shamrock fantasy, fantasy, vivid colors, grapevine, celtic fantasy art, lucky clovers, dreamlike atmosphere, captivating details, soft light and vivid colors')
    # Experimental
    EARTHBENDER = (28, "Earthbender", "EXPERIMENTAL",
                   ", earth elements, fantasy, rock, ground, grounding. A robust composition with earth elements, rocks and soil surrounding, highly detailed and realistic, cinematic lighting")
    AIRBENDER = (28, "Airbender", "EXPERIMENTAL",
                 ", air elements, fantasy, wind, clouds, liberating. A tranquil composition with air elements, wind gusts and floating clouds surrounding, highly detailed and realistic, cinematic lighting")
    METALBENDER = (28, "Metalbender", "EXPERIMENTAL",
                   ", metal elements, fantasy, metal, steel, tenacious. A sturdy composition with metal elements, shards and steel surrounding, highly detailed and realistic, cinematic lighting")
    BLOODBENDER = (28, "Bloodbender", "EXPERIMENTAL",
                   ", blood elements, fantasy, blood, body, unsettling. A dark composition with blood elements, veins and body fluid surrounding, highly detailed and realistic, cinematic lighting")
    LIGHTNINGBENDER = (28, "Lightbender", "EXPERIMENTAL",
                       ", lightning elements, fantasy, electricity, thunder, electrifying. A shocking composition with lightning elements, sparks and electricity surrounding, highly detailed and realistic, cinematic lighting")
    SPIRITBENDER = (28, "Spiritbender", "EXPERIMENTAL",
                    ", spirit elements, fantasy, spirit, ethereal, mystifying. A mystical composition with spirit elements, auras and spiritual energy surrounding, highly detailed and realistic, cinematic lighting")
    LAVABENDER = (28, "Lavabender", "EXPERIMENTAL",
                  ", lava elements, fantasy, molten rock, heat, blistering. A fierce composition with lava elements, molten rock and heat waves surrounding, highly detailed and realistic, cinematic lighting")
    WATERHEALER = (28, "Waterbender", "EXPERIMENTAL",
                   ", healing elements, fantasy, water, rejuvenation, restorative. A soothing composition with healing elements, glowing water and soothing vibes surrounding, highly detailed and realistic, cinematic lighting")

# KEY = (prompt, inspiration_thumb, style_id, seed)


class Inspiration(Enum):
    INSPIRATION_01 = ('sport car in the desert, vibrant',
                      'assets/inspirations/insp_70.webp', 28, 21)
    INSPIRATION_02 = ('dramatic dynamic portrait of Spider-Man covered in intricate floral bioluminescent spiderweb filigree, misty fantasy forest environment, bokeh ✨',
                      'assets/inspirations/insp_76.webp', 28, 530445)
    INSPIRATION_03 = ('milkyway in a glass bottle, 4K, unreal engine, octane render',
                      'assets/inspirations/insp_79.webp', 28, 738111)
    INSPIRATION_04 = ('sJames Christensen, style, portrait of a snow goddess, exquisite detail, 30-megapixel, 4k, 85-mm-lens, sharp-focus, intricately-detailed, long exposure time, f/8, ISO 100, shutter-speed 1/125, diffuse-back-lighting, award-winning photograph, facing-camera, looking-into-camera, monovisions, elle, small-catchlight, low-contrast, High-sharpness, symmetry, depth-of-field, golden-hour, ultra-detailed photography, shiny metal surface with intricate swirling mother of pearl inlays, raytraced, global illumination', 'assets/inspirations/insp_81.webp', 28, 829463)
    INSPIRATION_05 = ('realistic face, stunning model white purple ombré short bob hair, yellow dress Jacquemus, François Morellet inspired background, serene look, subtle smile, Sacai Nike, unearthing futuristic transparent fabrics, matte texture, octane render, full body shot fashion editorial photography, haute couture unprocessed cotton plant transparente dress, Louis Vuitton and Yayoi Kusama dots pattern style, pumpkin Yayoi Kusama, shades of light Yellow and white, with Louis Vuitton bag, on cyan studio background, ultra photorealistic + Hasselblad H6D + high definition + 8k + cinematic + color grading + depth of field + photo-realistic + film lighting', 'assets/inspirations/insp_72.webp', 28, 1312231)
    INSPIRATION_06 = ('a beautiful, charming young victorian woman, 24 years old, dark hair, bright eyes, gothic setting, sweet expression, with the face of charity wakefield, artwork by by atey ghailan, james gilleard, joe fenton, kaethe butcher, greg tocchini, vibrant colours', 'assets/inspirations/insp_71.webp', 28, 12322)
    INSPIRATION_07 = ('cloud wonderland, futuristic architecture, white, creme',
                      'assets/inspirations/insp_73.webp', 28, 743148)
    INSPIRATION_08 = ('wide-angle-split-photography of a ship inside of a bottle on the ocean, stormy, electrifying',
                      'assets/inspirations/insp_80.webp', 28, 669294)
    INSPIRATION_09 = ('musical house where the architecture inspired by a guitar, colorful lighting, ultra details, photography',
                      'assets/inspirations/insp_74.webp', 28, 113742)
    INSPIRATION_10 = ("Fauvism style Valentine's lovers strolling along the French Riviera Coastline, cinematic lighting",
                      'assets/inspirations/insp_75.webp', 28, 902287)
    INSPIRATION_11 = ('pretty face, bubbles penetrate beautiful white 16years old brunnet girl astronaut cracking the round space helmet surrounding her head, proportioned torso, full figure, nice legs, delicate face, Coby Whitmore',
                      'assets/inspirations/insp_77.webp', 28, 113768)
    INSPIRATION_12 = ('kneeling cat knight, portrait, finely detailed armor, intricate design, silver, silk, cinematic lighting, 4k,',
                      'assets/inspirations/insp_78.webp', 28, 653220)
    INSPIRATION_13 = ('Storm trooper as a vintagepunk samurai, dark grey background, blue and golden details, artstation, hyperdetailed, 8k, beautiful lighting, artstation by James Jean, Moebius, cory loftis, craig mullins, rutkowski, Mucha, hyperdetailed, over the shoulder, close up, james jean, mucha, fractal, vibrant colors, rococo art , 8k resolution, clear shape, defined shape, full body', 'assets/inspirations/insp_82.webp', 28, 91029)
    INSPIRATION_14 = ('gesture painting, guache on paper, female martial artist with bo staff, dynamic pose, professionally painted, in the style of Yoji Shinkawa',
                      'assets/inspirations/insp_83.webp', 28, 539989)
    INSPIRATION_15 = ('an alien city beneath a vantablack sun, by Quentin mabille, james jean,Takeshi Oga, dan mumford, eve ventrue, ayami kojima, artstation,epic scifi blackhole interplanetary spacecore , mysterious eeries ineffable mood, very detailed, negative space, massive scale, centered composition, anamorphic, 4k', 'assets/inspirations/insp_84.webp', 28, 654906)
    INSPIRATION_16 = ('a jewelry design,sakura-themed ring, gemstones and diamonds,luxury, closeup, product view,trending on artstation, cgsociety,ultra quality,digital art, exquisite hyper details,4k,Soft illumination, dreamy,fashion, rendering by unreal engine', 'assets/inspirations/insp_85.webp', 28, 73310)
    INSPIRATION_17 = ('full body, zoomed in to center, halo spartan wearing White spacex mechsuit, extremely detailed with rich colors Photography, Depth of Field, F/2.8, high Contrast, 8K, Cinematic Lighting, ethereal light, intricate details, extremely detailed, incredible details, full body, full colored, complex details, by Weta Digital, Photography, Photoshoot, Shot on 70mm, Depth of Field, DOF, 5D, Multiverse, Super-Resolution, ProPhoto RGB, Lonely, Good, Massive, Big, Spotlight, Frontlight, Halfrear Lighting, Backlight, Rim Lights, Rim Lighting, Natural Lighting, , Moody Lighting, Cinematic Lighting, volumetric Light, Volumetric Lighting, Volumetric, Contre-Jour', 'assets/inspirations/insp_86.webp', 28, 124591)
    INSPIRATION_18 = ('Award-winning concept art, a highly detailed a river rushing through a snowy ravine, winter trees, falling snow, chiaroscuro, hyperrealism, luminism, by Darek Zabrocki and Joseph McGurl and Bierstadt, hd, very detailed, 4k, 8k,', 'assets/inspirations/insp_87.webp', 28, 334284)
    INSPIRATION_19 = ('stunning vector art landscape, minimalism, red and white',
                      'assets/inspirations/insp_88.webp', 28, 981381)
    INSPIRATION_20 = ('biomechancial filament skull',
                      'assets/inspirations/insp_89.webp', 28, 899957)
    INSPIRATION_21 = ('illustration of psychadelic bear in a glowing enchanted forrest , (((by artist Sam Bosma)))',
                      'assets/inspirations/insp_90.webp', 28, 481654)
    INSPIRATION_22 = ('cute anime boy child dressing medieval cloths, dynamic pose, big and blue watery eyes, brown and short hair, digital art by rossdraws, brush strokes, painterly, impressionist style, half painted',
                      'assets/inspirations/insp_91.webp', 28, 573848)
    INSPIRATION_23 = ('cyberpunk tarot cart of hooded woman with a glowing rifle',
                      'assets/inspirations/insp_92.webp', 28, 962168)
    INSPIRATION_24 = ('fox adventurer figure, product shot, oil painting, whelan, beautiful lighting, fantasy, d&d, masterwork, realistic figure, realism, anthropomorphic figure,',
                      'assets/inspirations/insp_93.webp', 28, 359792)
    INSPIRATION_25 = ('stargate made of stone that form a circle, cinematic view, epic sky',
                      'assets/inspirations/insp_94.webp', 28, 628117)
    INSPIRATION_26 = ("An astronaut in a rose garden on a spring day, by martine johanna and simon stalenhag and chie yoshii and casey weldon and wlop : : ornate, dynamic, particulate, rich colors, intricate, elegant, highly detailed, harper's bazaar art, fashion magazine, smooth, sharp focus, 8 k, octane render, depth of view,", 'assets/inspirations/insp_95.webp', 28, 70000)
    INSPIRATION_27 = ('Dog doing yoga, yoga position, Full Frame,detailed, portraits, ultra sharp, depth of field, cinematic',
                      'assets/inspirations/insp_96.webp', 28, 148780)
    INSPIRATION_28 = ('A photo of astronaut in a jungle, cold color palette, muted colors, detailed, 8k, cinematic, dramatic colors, close-up',
                      'assets/inspirations/insp_43.webp', 28, 36999)
    INSPIRATION_29 = ('A black and white drawing of an astronaut, an ambient occlusion render by esao, cgsociety, space art, sci-fi, chillwave, ue5',
                      'assets/inspirations/insp_64.webp', 28, 77696)
    INSPIRATION_30 = ('close up portait beautiful girl the orange desert in modern fight suit, hyper realistic, pastel colors, complementary colors, muted colors, vibrant colors, dramatic colors, vaporwave, retrowave, black and white, colorfull, artochrome, highly detailed, 4k', 'assets/inspirations/insp_32.webp', 28, 440593)
    INSPIRATION_31 = ('assets/inspirations/insp_33.webp', 'a cat with wings, flyng over clouds, futuristic, elegant atmosphere, glowing lights, highly detailed, digital painting, artstaion, concept art, smooth sharp focus, illustration, art by wlop, mars ravelo,greg rutkowski', 28, 156337)
    INSPIRATION_32 = ('back to the future car, flying, Lightening, futuristic, elegant atmosphere, glowing lights, highly detailed, digital painting, artstaion, concept art, smooth sharp focus, illustration, art by wlop, mars ravelo,greg rutkowski', 'assets/inspirations/insp_34.webp', 28, 463788)
    INSPIRATION_33 = ('polymorph parametric Living Quarters on planet Jupiter, Interior Design, superb view of the planet, from the inside, Spacial Design, Futuristic, Patterns, Textures, Fluid, Massive, Detailed, Polished, Complex, Beautiful, Octane Rendering, Insane Graphics, 8k', 'assets/inspirations/insp_35.webp', 28, 113667)
    INSPIRATION_34 = ('The Last Ship Envy, steampunk, stylized digital illustration, sharp focus, elegant, intricate, digital painting, artstaion concept art, global illumination,ray tracing, advanced technology, chaykan howard, campion pascal,cooke darwin, davis jack, pink atmosphere', 'assets/inspirations/insp_36.webp', 28, 319577)
    INSPIRATION_35 = ('a painting of a purple owl sitting in a forest, trending on artstation, pixiv, dramatic, cinematic, 4k, highly detailed, mystic',
                      'assets/inspirations/insp_37.webp', 28, 437959)
    INSPIRATION_36 = ('a painting of a cute, iridescent ghost in a winter forest, futuristic, elegant atmosphere, glowing lights, highly detailed, digital painting, artstaion, concept art, smooth sharp focus, illustration, art by wlop, mars ravelo,greg rutkowski', 'assets/inspirations/insp_38.webp', 28, 649048)
    INSPIRATION_37 = ('a close up of a cat wearing a space suit, digital art, by Ryan Yee, zbrush central contest winner, 9gag, cute 3 d render, illustration of a cat, in style of nanospace, very detailed illustration, ruan cute vtuber, (extremely detailed, cute cartoon, with a space suit on', 'assets/inspirations/insp_39.webp', 28, 735177)
    INSPIRATION_38 = ('Futuristic cyberpunk masked assassin, half cyborg, riding a motorcycle, full body, in heavy rain, open road, neon lights, cyberpunk city, hyper realistic, unreal engine',
                      'assets/inspirations/insp_40.webp', 28, 370724)
    INSPIRATION_39 = ('A surreal time machine designed by dieter rams, product ad retro, colorful, futuristic, elegant atmosphere, glowing lights, highly detailed, digital painting, artstaion, concept art, smooth sharp focus, illustration, art by wlop, mars ravelo,greg rutkowski', 'assets/inspirations/insp_41.webp', 28, 646628)
    INSPIRATION_40 = ('Steampunk, ambulance, photorealistic, detailed, on a city street, in wartime, cinematic, dramatic colors, close-up, cgscociety, computer rendering, by mike winkelmann, uhd, rendered in cinema4d, hard surface modeling, 8k, render octane, inspired by beksinski', 'assets/inspirations/insp_42.webp', 28, 57459)
    INSPIRATION_41 = ('Cute and adorable cartoon goku baby, fantasy, dreamlike, surrealism, super cute, trending on artstation, cinematic, dramatic colors, close-up, cgscociety, computer rendering, by mike winkelmann, uhd, rendered in cinema4d, hard surface modeling, 8k,render octane, inspired by beksinski', 'assets/inspirations/insp_44.webp', 28, 252249)
    INSPIRATION_42 = ('Cute girl, with short, choppy hair and bangs, serene eyes, gentle eyebrows, slight smile, 4k, sharp focus, high resolution, by artgerm and greg rutkowski',
                      'assets/inspirations/insp_45.webp', 28, 734636)
    INSPIRATION_43 = ('modelshoot style, (extremely detailed CG unity 8k wallpaper), full shot body photo of the most beautiful artwork in the world, medieval armor, professional majestic oil painting by Ed Blinkey, Atey Ghailan, Studio Ghibli, by Jeremy Mann, Greg Manchess, Antonio Moro, trending on ArtStation, trending on CGSociety, Intricate, High Detail, Sharp focus, dramatic, photorealistic painting art by midjourney and greg rutkowski', 'assets/inspirations/insp_46.webp', 28, 979211)
    INSPIRATION_44 = ('diorama of a futuristic house made from a nautilus shell, concept art behance hd by jesper ejsing',
                      'assets/inspirations/insp_47.webp', 28, 609302)
    INSPIRATION_45 = ('dreamlikeart, modelshoot style, extremely detailed CG unity 8k, full body shot photo of the most beautiful artwork in the world, viking blonde shieldmaiden, beautiful blue eyes, sexy, winter, dark medieval, professional majestic oil painting by Atey Ghailan, by Jeremy Mann, Greg Manchess, Anthonis Mor, Studio Ghibli, ArtStation, CGSociety, Intricate, High Detail, Sharp focus, dramatic, photorealistic painting art by Midjourney and Greg Rutkowski', 'assets/inspirations/insp_48.webp', 28, 254039)
    INSPIRATION_46 = ('anthropomorphic art of a detective mouse, victorian inspired clothing by artgerm, victo ngai, ryohei hase, artstation. fractal papersand books. highly detailed digital painting, smooth, global illumination, fantasy art by greg rutkowsky, karl spitzweg', 'assets/inspirations/insp_49.webp', 28, 638726)
    INSPIRATION_47 = ('fantasy (mushroom girl), forest, (8k), beautiful, perfect, high quality, high detail, digital drawing, cute, blue, pretty face',
                      'assets/inspirations/insp_50.webp', 28, 448837)
    INSPIRATION_48 = ('An astronaut resting on mars in a beach chair, vibrant lighting, elegant, highly detailed, smooth, sharp focus, illustration, beautiful, geometric, trending on artstation, full body, cinematic, artwork by borovikovsky', 'assets/inspirations/insp_51.webp', 28, 282880)
    INSPIRATION_49 = ('Magic mad scientist, inside cosmic labratory, radiating a glowing aura stuff, loot legends, stylized, digital illustration, video game icon, artstation, lois van baarle, ilya kuvshinov, rossdraws',
                      'assets/inspirations/insp_52.webp', 28, 78861)
    INSPIRATION_50 = ('Photo of 8k ultra realistic lighthouse on island, heavy rain, night, light shining, heavy seas, full of colour, cinematic lighting, battered, trending on artstation, 4k, hyperrealistic, focused, extreme details, unreal engine 5, cinematic, masterpiece, art by studio ghibli', 'assets/inspirations/insp_53.webp', 28, 779494)
    INSPIRATION_51 = ('A study of cell shaded portrait of james cameron cyborg as borderlands 3 concept art, llustration, post grung, concept art by josan gonzales and wlop, by james jean, victo ngai, david rubin, mike mignola, laurie greasley, highly detailed, sharp focus, alien, trending on artstation, hq, deviantart, art by artgem', 'assets/inspirations/insp_54.webp', 28, 740685)
    INSPIRATION_52 = ('A demon girl with big and cute eyes, || very anime, fine-face, realistic shaded perfect face, fine details. anime. realistic shaded lighting poster by ilya kuvshinov katsuhiro otomo ghost-in-the-shell, magali villeneuve, artgerm, jeremy lipkin and michael garmash, rob rey and kentarõ miura style, trending on art station', 'assets/inspirations/insp_55.webp', 28, 878148)
    INSPIRATION_53 = ('A futuristic shoe designed by nike, cinematic, dramatic colors, close-up, cgscociety, computer rendering, by mike winkelmann, uhd, rendered in cinema4d, hard surface modeling, 8k, render octane, inspired by beksinski', 'assets/inspirations/insp_56.webp', 28, 969439)
    INSPIRATION_54 = ("A cute adorable baby owl made of crystal ball with low poly eye's highly detailed intricated concept art trending artstation 8k, cinematic, dramatic colors, close-up, cgscociety, computer rendering, by mike winkelmann, uhd, rendered in cinema4d", 'assets/inspirations/insp_57.webp', 28, 718284)
    INSPIRATION_55 = ('Se7een design studio in a modern cool font and 3d metalic pastel, futuristic, elegant atmosphere, glowing lights, highly detailed, digital painting, artstaion, concept art, smooth sharp focus, illustration, art by wlop, mars ravelo,greg rutkowski', 'assets/inspirations/insp_58.webp', 28, 856963)
    INSPIRATION_56 = ('A miniature tabletop a pleasant christmas time canada landscape, snow, trees, christmas shop, glowing under an ornate glass dome, by paulette tavormina and michael whelan and donato giancola, inside a dusty abandoned laboratory, hyper realistic, extremely detailed, dramatic lighting, victorian, unreal engine, featured on artstation, octane rendar', 'assets/inspirations/insp_59.webp', 28, 514654)
    INSPIRATION_57 = ('Interior of luxury condominium with minimalist furniture and lush house plants and abstract wall paintings | modern architecture by makoto shinkai, ilya kuvshinov, lois van baarle, rossdraws and frank lloyd wright',
                      'assets/inspirations/insp_60.webp', 28, 307235)
    INSPIRATION_58 = ('Cartoony, happy joe rogan portrait painting of a rabbit character from overwatch, armor, girly pink color scheme design, full shot, asymmetrical, splashscreen, organic painting, sunny day, matte painting, bold shapes, hard edges, cybernetic, moon in background, street art, trending on artstation, by huang guangjian and gil elvgren and sachin teng', 'assets/inspirations/insp_61.webp', 28, 696433)
    INSPIRATION_59 = ('Dark minimalist background with 3d geometry dunes desert with flying cubes and pyramids abstract neon vector colored degraded gradient abstract hdr, uhd, 4k, 8k trending on artstation and deviantart bokeh',
                      'assets/inspirations/insp_62.webp', 28, 73896)
    INSPIRATION_60 = ('.your thoughts become your reality cloud, sky, and sun in the background, palms, see. renaissance aesthetic, star trek aesthetic, pastel colors aesthetic, intricate fashion clothing, highly detailed, surrealistic, digital painting, concept art, sharp focus, illustration, unreal engine art by artgerm and greg rutkowski', 'assets/inspirations/insp_63.webp', 28, 968698)
    INSPIRATION_61 = ('Side view cyber vehicle white isolated background futuristic design,  futuristic, elegant atmosphere, glowing lights, highly detailed, digital painting, artstaion, concept art, smooth sharp focus, illustration, art by wlop, mars ravelo, greg rutkowski', 'assets/inspirations/insp_65.webp', 28, 536900)
    INSPIRATION_62 = ('A photo of Pikachu in interstellar movie, cinematic, dramatic colors, close-up, cgscociety, computer rendering, by mike winkelmann, uhd, rendered in cinema4d, hard surface modeling, 8k, render octane, inspired by beksinski', 'assets/inspirations/insp_66.webp', 28, 195176)
    INSPIRATION_63 = ('Cute stylish pikachu dressed in stylish futuristic sportswear clothes, big sneakers and a futuristic glasses, cinematic, dramatic colors, close-up, cgscociety, computer rendering, by mike winkelmann, uhd, rendered in cinema4d, hard surface modeling, 8k, render octane, inspired by beksinski', 'assets/inspirations/insp_67.webp', 28, 362884)
    INSPIRATION_64 = ('A photo of Batman sitting on a roof looking down at a city below, extremely detailed, gotham, gloomy, dark',
                      'assets/inspirations/insp_68.webp', 28, 540588)
    INSPIRATION_65 = ('Highly detailed, digital painting, atmospheric lighting, octane render, unreal engine, professional, eagle owl metal beak fantasy mystery sick,  cinematic, dramatic colors, close-up, cgscociety, computer rendering, by mike winkelmann, uhd, rendered in cinema4d, hard surface modeling, 8k,render octane, inspired by beksinski', 'assets/inspirations/insp_69.webp', 28, 462024)
