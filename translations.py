import json
import re


translations = {

    # messages by Lucas Werkmeister
    'en': {
        'create': 'Create',
        'csrf_warning': 'Sorry, we couldn’t process this request (<abbr title="Cross-site request forgery">CSRF</abbr> protection failed). Please try submitting the form again.',
        'duplicates_warning': 'The following existing {lexemes!p:one=lexeme has:other=lexemes have} the same lemma and language code as the one you’re trying to create:',
        'duplicates_instructions': 'If you’re sure that {lexemes!p:one=it’s:other=they’re} different, check the box at the bottom of the form.',
        'no_duplicate': 'This is not a duplicate of an existing lexeme.',
        'advanced': 'Advanced',
        'advanced_general': 'You are in “advanced” mode.',
        'advanced_lexeme_id': 'You can enter a lexeme ID to add forms to an existing lexeme instead of creating a new one. Leave any forms that already exist on the lexeme blank, otherwise they will be duplicated!',
        'advanced_partial_forms': 'You can leave some forms blank so that they will not be added. Make sure you’re not accidentally leaving out any forms!',
        'lexeme_id': 'Lexeme ID',
        'advanced_partial_forms_hint': 'To create lexemes with some forms missing, switch to advanced mode.',
        'generated_via': 'generated via',
        'description_with_forms_and_senses': '{description}, {forms!p:0=no forms:one=one form:other={forms} forms} and {senses!p:0=no senses:one=one sense:other={senses} senses}',
        'bulk_link': 'bulk mode',
        'bulk_button': 'Bulk mode',
        'bulk_heading': 'bulk mode',
        'bulk_format_help': 'format help',
        'bulk_not_allowed': 'You are not allowed to use bulk mode. Sorry.',
        'edit_button': 'Edit',
        'edit_link': 'edit',
        'edit_general': 'You are in “edit” mode. Changing the values below will edit, add or remove forms of the target lexeme.',
        'edit_mismatch_warning': 'This lexeme does not appear to match this template! Please double-check that it is the right template for this lexeme before continuing.',
        'edit_ambiguous_warning': 'The following lexeme {forms!p:one=form:other=forms} matched more than one template form equally well:',
        'edit_unmatched_warning': 'The following lexeme {forms!p:one=form:other=forms} did not match any of the template forms:',
        'edit_form_list_item': '{form_link}, {grammatical_feature_labels!l}, {statements!p:0=no statements:one=one statement:other={statements} statements}',
        'no_grammatical_features': 'no grammatical features',
    },

    # translations by User:Oriciu, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Asturian
    'ast': {
        'create': 'Crear',
        'csrf_warning': 'Sentímoslo, nun pudimos procesar la solicitú (falló la protección escontra <abbr title="Cross-site request forgery">CSRF</abbr>). Tenta volver a unviar el formulariu.',
        'duplicates_warning': 'Los lexemes siguientes tienen yá un llema y códigu d\'idioma iguales que\'l que tentes crear:',
        'duplicates_instructions': 'Si tas seguru de que son distintos, marca\'l caxellu d\'abaxo del formulariu.',
        'no_duplicate': 'Esti lexema nun ye un duplicáu d\'otru esistente.',
        'advanced': 'Avanzao',
        'advanced_general': 'Tas en mou «avanzáu».',
        'advanced_lexeme_id': 'En llugar de crear un lexema nuevu, puedes escribir un identificador de lexema p\'añadir formes al mesmu. ¡Dexa en blancu les formes del lexema que yá existan, o crearás duplicaos!',
        'advanced_partial_forms': 'Puedes dexar en blancu delles formes pa que nun s\'añadan. ¡Asegúrate de nun escaecer nenguna forma accidentalmente!',
        'lexeme_id': 'Identificador',
    },

    # translations by User:Bodhisattwa, User:Tanay barisha and User:Mahir256, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Bengali
    'bn': {
        'create': 'তৈরি করুন',
        'csrf_warning': 'দুঃখিত, আমরা এই অনুরোধটির প্রক্রিয়াকরণ করতে পারিনি (<abbr title="ক্রস-সাইট অনুরোধ জালিয়াতি">সিএসআরএফ</abbr> সংরক্ষণকরণ ব্যর্থ)। দয়া করে আবার ফর্মটি জমা দিন।',
        'duplicates_warning': 'আপনি যে লেক্সিম তৈরি করতে চাইছেন তার অনুরূপ লেমা এবং ভাষা-কোড নিম্নলিখিত লেক্সিমগুলিতে রয়েছে :',
        'duplicates_instructions': 'আপনি যদি নিশ্চিত হন যে এগুলি ভিন্ন, তাহলে ফর্মের নীচে বাক্সটি টিক চিহ্নিত করুন।',
        'no_duplicate': 'এটি বিদ্যমান কোন লেক্সিমের সদৃশ নয়।',
        'advanced': 'উন্নত',
        'advanced_general': 'আপনি "উন্নত" প্রণালী ব্যবহার করছেন।',
        'advanced_lexeme_id': 'নতুন লেক্সিম তৈরি করার পরিবর্তে কোন বিদ্যমান লেক্সিমের আইডি লিখে সেটির শব্দরূপ যোগ করতে পারেন। বিদ্যমান শব্দরূপের ক্ষেত্রগুলি ফাঁকা রাখুন, নতুবা সেটির সদৃশ আরেকটি শব্দরূপ তৈরি হবে!',
        'advanced_partial_forms': 'কোন শব্দরূপ যোগ করতে না চাইলে সেটি ফাঁকা রাখতে পারেন। তবে এটা নিশ্চিত করুন যে আপনি ভুলবশত কোন শব্দরূপ ছেড়ে যাচ্ছেন না।',
        'lexeme_id': 'লেক্সিম আইডি',
        'advanced_partial_forms_hint': 'যদি এমন লেক্সিম তৈরি করতে চান, যেটির কিছু শব্দরূপ অনুপস্থিত, তবে "উন্নত" প্রণালী ব্যবহার করুন।',
        'generated_via': 'যার মাধ্যমে উৎপন্ন',
        'description_with_forms_and_senses': '{description}, {forms!p:0=শব্দরূপ নেই:one=একটি শব্দরূপ:other={forms}টি শব্দরূপ} ও {senses!p:0=অর্থ নেই:one=একটি অর্থ:other={senses}টি অর্থ}',
        'bulk_link': 'গণহার প্রক্রিয়া',
        'bulk_button': 'গণহার প্রক্রিয়া',
        'bulk_heading': 'গণহার প্রক্রিয়া',
        'bulk_format_help': 'বিন্যাস সাহায্য',
        'bulk_not_allowed': 'আপনার গণহার প্রক্রিয়া ব্যবহারের অনুমতি নেই। দুঃখিত।',
        'edit_button': 'সম্পাদনা করুন',
        'edit_link': 'সম্পাদনা করুন',
        'edit_general': 'আপনি সম্পাদনা মোডে রয়েছেন। নীচের মানগুলি পরিবর্তন করলে লেক্সিমটির শব্দরূপ সম্পাদনা, যোগ বা অপসারণ করা যাবে।',
        'edit_mismatch_warning': 'এই লেক্সিম এই টেমপ্লেটের সঙ্গে সামঞ্জস্যপূর্ণ বলে মনে হচ্ছে না! দয়া করে এগোনোর আগে এটি সঠিক টেমপ্লেট কিনা আরেকবার যাচাই করে নিন।',
        'edit_ambiguous_warning': 'পরবর্তী লেক্সিমটির {forms!p:one=শব্দরূপটি:other=শব্দরূপগুলি} একাধিক টেমপ্লেটের সঙ্গে সমানভাবে সামঞ্জস্য রক্ষা করছে:',
        'edit_unmatched_warning': 'পরবর্তী লেক্সিমটির {forms!p:one=শব্দরূপটি:other=শব্দরূপগুলি} কোন টেম্পলেটের সঙ্গে সামঞ্জস্য রক্ষা করছে না:',
        'edit_form_list_item': '{form_link}, {grammatical_feature_labels!l}, {statements!p:0=বিবৃতি নেই:one=একটি বিবৃতি:other={statements}টি বিবৃতি}',
        'no_grammatical_features': 'কোন ব্যাকরণগত বৈশিষ্ট্য নেই',
    },

    # translations by User:VIGNERON, User:Fulup and User:Iriep, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Breton
    'br': {
        'create': 'Krouiñ',
        'csrf_warning': 'N\'eus ket bet gallet ober war-dro ar reked-mañ (gwarez <abbr title="Cross-site request forgery">CSRF</abbr> c\'hwitet). Klaskit adkas ar furm.',
        'duplicates_warning': 'Al leksemoù da heul o deus an hevelep lemma, ha kod yezh, hag an hini emaoc\'h o klask krouiñ:',
        'duplicates_instructions': 'Mard oc\'h sur int disheñvel, askit al log e traoñ ar furm.',
        'no_duplicate': 'N\'eo ket un eil eus ul leksem a zo anezhañ c\'hoazh.',
        'advanced': 'Araokaet',
        'advanced_general': 'Er mod “araokaet” emaoc\'h.',
        'advanced_lexeme_id': 'Gallout a rit merkañ ID ul leksem evit ouzhpennañ furmoù d\'ul leksem a zo anezhañ, kentoc\'h eget krouiñ unan nevez. Lezit goullo kement furm a zo anezhi c\'hoazh war al leksem a-hend-all e vint eilet!',
        'advanced_partial_forms': 'Gallout a rit lezel goullo furmoù \'zo, evel-se ne vint ket ouzhpennet. Bezit sur na lezit ket furmoù er-maez dre fazi!',
        'lexeme_id': 'ID al leksem',
        'advanced_partial_forms_hint': 'Evit krouiñ leksemoù gant furmoù a vank, grit gant ar mod araokaet.',
        'generated_via': 'ganet dre',
        # 'description_with_forms_and_senses': '{description}, {forms!p:0=no forms:one=ur furm|other={forms} furm} ha {senses!p:0=ster ebet:one=ur ster:other={senses} senses}',
        'bulk_link': 'mod a-vras',
        'bulk_button': 'Mod a-vras',
        'bulk_heading': 'mod a-vras',
        'bulk_format_help': 'Skoazell furmad',
        'bulk_not_allowed': 'N\'oc\'h ket aotreet d\'ober gant ar mod a-vras.',
        'edit_button': 'Aozañ',
        'edit_link': 'aozañ',
        'edit_general': 'Emaoc\'h er mod “aozañ”. Ma cheñchit an talvoudoù dindan e vo aozet, ouzhpennet pe dilamet furmoù \'zo eus al leksem pal.',
        'edit_mismatch_warning': 'Evit doare ne glot ket al leksem-mañ gant ar patrom! Gwiriit mat eo ar patrom a zere evit al leksem a-raok kenderc\'hel ganti.',
        # 'edit_ambiguous_warning': '{forms!p:one=furm:other=a furmoù} al leksem da heul a glote kement ha kement gant furm meur a batrom:',
        # 'edit_unmatched_warning': '{forms!p:one=Furm:other=Furmoù} al leksem da heul ne {forms!p:one=glote:other=glotent} gant furm ebet eus ar patrom:',
        # 'edit_form_list_item': '{form_link}, {grammatical_feature_labels!l}, {statements!p:0=disklêriadur ebet:one=un disklêriadur:other={statements} disklêriadur}',
        'no_grammatical_features': 'perzh yezhadurel ebet',
    },

    # translations by User:Lexicolover, User:Matěj Suchánek and User:Adrijaned, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Czech
    'cs': {
        'create': 'Vytvořit',
        'csrf_warning': 'Bohužel se nám nepodařilo vykonat požadavek (ochrana před <abbr title="Cross-site request forgery">CSRF</abbr> selhala). Zkuste prosím odeslat formulář znovu.',
        'duplicates_warning': 'Pokoušíte se vytvořit lexém, který má stejné lemma a jazyk jako už existující lexémy:',
        'duplicates_instructions': 'Jste-li si jisti, že zadávaný lexém je odlišný, zatrhněte pole na konci formuláře.',
        'no_duplicate': 'Tento lexém není duplicitní k již existujícímu lexému.',
        'advanced': 'Pokročilé',
        'advanced_general': 'Nacházíte se v „pokročilém“ režimu.',
        'advanced_lexeme_id': 'Zde můžete zadat ID lexému, ke kterému chcete přidat chybějící tvary, namísto vytvoření nového. Veškeré tvary, které jsou již u lexému vyplněné, nechte prázdné, jinak budou vytvořeny jako duplicitní!',
        'advanced_partial_forms': 'Některé tvary můžete nechat prázdné a tyto pak nebudou přidány do lexému. Ujistěte se, že omylem nevynecháte některý tvar!',
        'lexeme_id': 'ID lexému',
        'advanced_partial_forms_hint': 'Chcete-li vytvořit lexém bez některých tvarů, přepněte do pokročilého režimu.',
        'generated_via': 'vygenerováno pomocí',
        'description_with_forms_and_senses': '{description}, {forms!p:0=žádné tvary:one=jeden tvar:few={forms} tvary:other={forms} tvarů} a {senses!p:0=žádné významy:one=jeden význam:few={senses} významy:other={senses} významů}',
        'bulk_link': 'hromadný mód',
        'bulk_button': 'Hromadný mód',
        'bulk_heading': 'hromadný mód',
        'bulk_format_help': 'nápověda k formátování',
        'bulk_not_allowed': 'Litujeme, ale nemáte oprávnění k použití hromadného módu.',
        'edit_button': 'Editovat',
        'edit_link': 'editovat',
        'edit_general': 'Nacházíte se v módu editace. Upravování hodnot níže povede k upravení, přidání, nebo odebrání tvarů z cílového lexému.',
        'edit_mismatch_warning': 'Zdá se, že tento lexém neodpovídá tomuto vzoru! Prosím, zkontrolujte si, že opravdu používáte správný vzor před tím, než budete pokračovat!',
        'edit_ambiguous_warning': 'Následující {forms!p:one=tvar:few=tvary:other=tvary} lexému odpovídají více než jednomu vzoru se stejnou pravděpodobností:',
        'edit_unmatched_warning': 'Následující {forms!p:one=tvar:few=tvary:other=tvary} lexému neodpovídají ani jednomu ze vzorů:',
        'edit_form_list_item': '{form_link}, {grammatical_feature_labels!l}, {statements!p:0=žádná tvrzení:one=jedno tvrzení:few={statements} tvrzení:other={statements} tvrzení}',
        'no_grammatical_features': 'bez gramatických vlastností',
    },

    # translations by User:So9q and User:Fnielsen, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Danish
    'da': {
        'create': 'Opret',
        'csrf_warning': 'Din anmodning kunne ikke fremsættes på grund af en <abbr title="Cross-site request forgery">CSRF</abbr>-fejl. Prøv igen.',
        'duplicates_warning': 'Disse eksisterende leksemer har den samme ordstamme og sprogkode som den, du prøver at oprette:',
        'duplicates_instructions': 'Hvis du er sikker på, at de er forskellige, skal du markere afkrydsningsfeltet i bunden af formularen.',
        'no_duplicate': 'Dette er ikke en duplikat af et eksisterende leksem.',
        'advanced': 'Avanceret',
        'advanced_general': 'Du er i “avanceret” tilstand',
        'advanced_lexeme_id': 'Her kan du indtaste et leksem-id for at tilføje formularer til et eksisterende leksem i stedet for at oprette et nyt. For at undgå duplikering af eksisterende formularer skal du lade disse felter være tomme.',
        'advanced_partial_forms': 'Du kan lade nogle felter være tomme; så tilføjes disse formularer ikke. Sørg dog for, at du ikke efterlader nogen felter tomme ved en fejltagelse!',
        'lexeme_id': 'Leksem-ID',
        'advanced_partial_forms_hint': 'For at oprette leksem uden at udfylde alle felter skal du skifte til avanceret tilstand.',
        'generated_via': 'oprettet gennem',
        'description_with_forms_and_senses': '{description}, {forms!p:0=ingen forme:one=en form:other={forms} forme} og {senses!p:0=inge betydelser:one=en betydelse:other={senses} betydelser}',
        'bulk_link': 'masseopret',
        'bulk_button': 'Masseopret',
        'bulk_heading': 'masseopret',
        'bulk_format_help': 'formateringshjælp',
        'bulk_not_allowed': 'Desværre har du ikke tilladelse til at oprette flere leksemer samtidigt.',
    },

    # translations by Lucas Werkmeister
    'de': {
        'create': 'Anlegen',
        'csrf_warning': 'Entschuldigung, wir konnten diese Anfrage nicht verarbeiten (<abbr title="Cross-site request forgery">CSRF</abbr>-Schutz schlug fehl). Bitte versuche, das Formular nochmal abzuschicken.',
        'duplicates_warning': '{lexemes!p:one=Das folgende, bereits bestehende Lexem hat:other=Die folgenden, bereits bestehenden Lexeme haben} das gleiche Lemma und den gleichen Sprachcode wie das, was du erstellen willst:',
        'duplicates_instructions': 'Wenn du sicher bist, dass es {lexemes!p:one=ein unterschiedliches Lexem ist:other=unterschiedliche Lexeme sind}, kreuze das Kästchen am Ende des Formulars an.',
        'no_duplicate': 'Dies ist kein Duplikat eines existierenden Lexems.',
        'advanced': 'Erweitert',
        'advanced_general': 'Du befindest dich im „erweiterten“ Modus.',
        'advanced_lexeme_id': 'Du kannst eine Lexem-ID eingeben, um Formen zu einem bestehenden Lexem hinzuzufügen, anstatt ein neues zu erstellen. Lass alle Formen, die das Lexem bereits hat, leer, sonst werden sie dupliziert!',
        'advanced_partial_forms': 'Du kannst einige Formen leer lassen, so dass sie nicht hinzugefügt werden. Stelle sicher, dass du nicht aus Versehen welche weglässt!',
        'lexeme_id': 'Lexem-ID',
        'advanced_partial_forms_hint': 'Um Lexeme zu erstellen, denen einige Formen fehlen, wechsle in den erweiterten Modus.',
        'generated_via': 'generiert durch',
        'description_with_forms_and_senses': '{description}, {forms!p:0=keine Formen:one=eine Form:other={forms} Formen}, {senses!p:0=keine Senses:one=ein Sense:other={senses} Senses}',
        'edit_button': 'Bearbeiten',
        'edit_link': 'bearbeiten',
        'edit_general': 'Du befindest dich im „Bearbeiten“-Modus. Wenn du die Werte unten bearbeitest, werden Formen des Ziellexems geändert, hinzugefügt oder entfernt.',
        'edit_mismatch_warning': 'Dieses Lexem scheint nicht zu dieser Vorlage zu passen! Bitte prüfe nochmal genau nach, dass es die richtige Vorlage für dieses Lexem ist, bevor du fortfährst.',
        'edit_ambiguous_warning': 'Die {forms!p:one=folgende Lexem-Form passt:other=folgenden Lexem-Formen passen} zu mehreren Formen der Vorlage gleich gut:',
        'edit_unmatched_warning': 'Die {forms!p:one=folgende Lexem-Form passt:other=folgenden Lexem-Formen passen} zu keinen Formen der Vorlage:',
        'edit_form_list_item': '{form_link}, {grammatical_feature_labels!l}, {statements!p:0=keine Aussagen:one=eine Aussage:other={statements} Aussagen}',
        'no_grammatical_features': 'keine grammatikalischen Funktionen',
    },

    # translations by User:Jens Ohlig and User:Robin van der Vliet, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Esperanto
    'eo': {
        'create': 'Krei',
        'csrf_warning': 'Pardonu, ni ne povis procesi ĉi tiun peton (protekto kontraŭ <abbr title="Cross-site request forgery">CSRF</abbr> malsucesis). Bonvolu provi submeti la formularon denove.',
        'duplicates_warning': 'La jenaj ekzistantaj leksemoj havas saman lemo kaj lingva kodo kiel tiu kiun vi provis krei:',
        'duplicates_instructions': 'Se vi certas, ke ili estas malsamaj, marku la markobutonon ĉe la malsupro de la formo.',
        'no_duplicate': 'Ĉi tiu ne estas duplikato de ekzistanta leksemo.',
        'advanced': 'Altnivela reĝimo',
        'advanced_general': 'Vi estas en “altnivela” reĝimo.',
        'advanced_lexeme_id': 'Vi povas enmeti lekseman identifikilon por aldoni formojn al ekzistanta leksemo anstataŭ krei novan leksemon. Lasu formojn kiuj jam ekzistas pri tio leksemo malplenajn, alie la formoj estos duobligitaj!',
        'advanced_partial_forms': 'Vi povas lasi iujn formojn malplenaj por ke ili ne aldoniĝos. Certiĝu, ke vi hazarde ne lasas iun formojn!',
        'lexeme_id': 'Leksema identifikilo',
        'advanced_partial_forms_hint': 'Por krei leksemojn kun mankantaj formoj, ŝanĝu al altnivela reĝimo.',
        'edit_button': 'Redakti',
        'edit_link': 'redakti',
        'edit_form_list_item': '{form_link}, {grammatical_feature_labels!l}, {statements!p:0=neniu deklaro:one=unu deklaro:other={statements} deklaroj}',
        'no_grammatical_features': 'neniu gramatika trajto',
    },

    # translations by User:Andreasmperu, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Spanish
    'es': {
        'create': 'Crear',
        'csrf_warning': 'Lo siento, esta solicitud no pudo ser procesada (<abbr title="Cross-site request forgery">CSRF</abbr> protection failed). Por favor, intenta enviar el formulario nuevamente.',
        'duplicates_warning': 'Los lexemas siguientes ya tienen un lema y un código lingüístico idéntico a aquel que estás intentado crear:',
        'duplicates_instructions': 'Si estás seguro que son distintos, revisa la casilla situada al final de este formulario.',
        'no_duplicate': 'Este no es un duplicado de un lexema existente.',
        'advanced': 'Avanzado',
        'advanced_general': 'Estás en el modo "avanzado".',
        'advanced_lexeme_id': 'En lugar de crear un nuevo lexema, puedes ingresar el identificador de un lexema existente para añadir las formas faltantes. Deja en blanco las formas ya existentes en el lexema; de lo contrario, ¡se creará un duplicado!',
        'advanced_partial_forms': 'Puedes dejar algunas formas en blanco para evitar que sean añadidas. ¡Asegúrate de crear todas las formas necesarias!',
        'lexeme_id': 'Identificador de lexema',
    },

    # translations by User:Reosarevok, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Estonian
    'et': {
        'create': 'Loo',
        'csrf_warning': 'Vabandust, taotluse töötlemine ebaõnnestus (<abbr title="Cross-site request forgery">CSRFi</abbr> vastane kaitse ebaõnnestus). Palun proovi vorm uuesti saata.',
        'duplicates_warning': 'Nendel olemasolevatel lekseemidel on sama lemma ja keel kui lekseemil, mida sa tahad luua:',
        'duplicates_instructions': 'Kui sa oled kindel, et nad on erinevad, märgi vormi lõpus olev märkeruut.',
        'no_duplicate': 'See lekseem pole sama kui olemasolevad lekseemid.',
        'advanced': 'Laienda',
        'advanced_general': 'Oled laiendatud režiimis',
        'advanced_lexeme_id': 'Saad sisestada olemasoleva lekseemi ID, et lisada rohkem vorme. Jäta tühjaks need vormid, mis on juba lekseemis olemas, vastasel juhul lisatakse need duplikaatidena.',
        'advanced_partial_forms': 'Saad vormid tühjaks jätta, et neid ei lisataks. Kontrolli aga, et sa ei jätnud mõnda vormi kogemata tühjaks!',
        'lexeme_id': 'Lekseemi ID',
    },

    # translations by User:Theklan, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Basque
    'eu': {
        'create': 'Sortu',
        'csrf_warning': 'Barkatu, ezin izan dugu zure eskaera prozesatu (<abbr title="Cross-site request forgery">CSRF</abbr> babesak huts egin du). Saia zaitez berriro ere eskaera bidaltzen.',
        'duplicates_warning': 'Dagoeneko badugu hizkuntza kode berberarekin lema berdina duten lexema hauek:',
        'duplicates_instructions': 'Ziur bazaude lexema ezberdina dela, klik egin goian dagoen formularioko kutxan.',
        'no_duplicate': 'Hau ez da bikoiztutako lexema bat.',
        'advanced': 'Aurreratua',
        'advanced_general': 'Modu "aurrearatuan" zaude.',
        'advanced_lexeme_id': 'Lexema ID bat sar dezakezu dagoeneko existitzen den lexema bati formak gehitzeko, berri bat sortu beharrean. Dagoeneko existitzen diren lexemen formak zuriz utzi, bestela bikoiztuko dira eta!',
        'advanced_partial_forms': 'Formularioko atal batzuk zuriz utzi ditzakezu, eta ez dira gehituko. Ziurtatu ez zaudela nahi gabe formarik ahazten!',
        'lexeme_id': 'Lexema ID',
        'advanced_partial_forms_hint': 'Forma batzuk falta dituzten lexemak sortzeko, aukeratu modu aurreratua',
        'generated_via': 'honen bidez sortua',
        'description_with_forms_and_senses': '{description}, {forms!p:0=formarik ez:one=forma bat:other={forms} forma} eta {senses!p:0=esanahirik ez:one=esanahi bat:other={senses} esanahi}',
    },

    # translations by User:Ladsgroup, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Persian
    'fa': {
        'create': 'ایجاد',
        'csrf_warning': 'شرمنده، ما قادر به پردازش این درخواست نیستیم. (حفاظت <abbr title="Cross-site request forgery" lang="en" dir="ltr">CSRF</abbr> به خطا خورد). لطفا دوباره این فرم را بفرستید.',
        'duplicates_warning': 'این تکواژه‌ها مدخل و زبان یکسانی با تکواژه‌ای که قصد ساختنش را دارید دارند:',
        'duplicates_instructions': 'اگر مطمئنید که این تکواژه‌ها متفاوت هستند، جعبه پایین فرم را علامت بزنید.',
        'no_duplicate': 'این یک تکواژه تکراری نیست.',
        'advanced': 'پیشرفته',
        'advanced_general': 'شما در حالت پیشرفته هستید.',
        'advanced_lexeme_id': 'شما می‌توانید یک شماره تکواژ وارد کنید تا فرم‌های جدید به آن اضافه کنید. هر فرمی که قبلا در صفحه تکواژه موجود است خالی بگذارید، در غیر این صورت کپی خواهند شد.',
        'advanced_partial_forms': 'شما می‌توانید بخشی از فرم‌ها را خالی بگذارید و در این صورت آنها اضافه نخواهند شد. مطمئن شوید که هیچ فرمی تصادفا خالی نمی‌گذارید.',
        'lexeme_id': 'شماره تکواژه',
        'advanced_partial_forms_hint': 'برای ایجاد تکواژه بدون بخشی از فرم‌هایش، به حالت پیشرفته سوییچ کنید.',
        'generated_via': 'تولید شده با استفاده از',
        'description_with_forms_and_senses': '{description}، {forms!p:0=بدون فرم:one=یک فرم:other={forms} فرم} و {senses!p:0=بدون معنی:one=یک معنی:other={senses} معنی}',
        'bulk_link': 'ویرایش انبوه',
        'bulk_button': 'ویرایش انبوه',
        'bulk_heading': 'ویرایش انبوه',
        'bulk_format_help': 'راهنمای قالب‌بندی',
        'bulk_not_allowed': 'شما دسترسی لازم برای استفاده از ویرایش انبوه را ندارید. شرمنده.',
    },

    # translations by User:Shinnin, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Finnish
    'fi': {
        'create': 'Julkaise',
        'csrf_warning': 'Anteeksi, pyynnön käsittely ei onnistunut (<abbr title="Cross-site request forgery">CSRF</abbr> suojaus epäonnistui). Yritä tallentaa kaavake uudestaan, kiitos.',
        'duplicates_warning': 'Seuraavilla lekseemeillä on sama lemma ja kieli kuin sillä, jota yrität luoda:',
        'duplicates_instructions': 'Jos olet varma, että ne ovat eri lekseemeitä, laita rasti kaavakkeen lopussa olevaan laatikkoon.',
        'no_duplicate': 'Tämä ei ole kaksoiskappale olemassa olevasta lekseemistä.',
        'advanced': 'Laajenna',
        'advanced_general': 'Olet laajennetussa muokkaustilassa.',
        'advanced_lexeme_id': 'Uuden lekseemin luomisen lisäksi voit muokata jo olemassa olevaa lekseemiä syöttämällä sen tunnisteen. Jätä lekseemissä jo olevat taivutusmuodot tyhjiksi, muuten ne tuplaantuvat.',
        'advanced_partial_forms': 'Voit jättää jotkin taivutusmuodoista tyhjiksi. Varmista kuitenkin, että ne ovat tyhjiä tarkoituksella eivätkä vahingossa.',
        'lexeme_id': 'Lekseemi-tunniste',
        'advanced_partial_forms_hint': 'Luodaksesi lekseemin ilman joitakin taivutusmuotoja, siirry laajennettuun muokkaustilaan.',
    },

    # translations by User:Djiboun, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/French
    'fr': {
        'create': 'Créer',
        'csrf_warning': 'Désolé, cette requête n\'a pas pu être traitée (la protection anti-<abbr title="Cross-site request forgery">CSRF</abbr> a échoué). Essayez de renvoyer le formulaire.',
        'duplicates_warning': 'Les lexèmes suivants possèdent déjà un lemme et un code de langue identiques à celui que vous souhaitez créer :',
        'duplicates_instructions': 'Si vous êtes certains qu\'ils sont différents, cochez la case située en fin de formulaire.',
        'no_duplicate': 'Ceci n\'est pas le doublon d\'un lexème existant.',
        'advanced': 'Avancé',
        'advanced_general': 'Vous êtes dans le mode "avancé".',
        'advanced_lexeme_id': 'Au lieu de créer un nouveau lexème, vous pouvez entrer l\'identifiant d\'un lexème existant pour y ajouter des formes supplémentaires. Laissez les cases vides pour les formes déjà existantes afin d\'éviter de créer des doublons !',
        'advanced_partial_forms': 'Vous pouvez laisser des cases vides pour empêcher la création des formes associées. Assurez-vous de ne pas oublier accidentellement l\'une des formes !',
        'lexeme_id': 'Identifiant',
        'advanced_partial_forms_hint': 'Pour créer des lexèmes en laissant certaines formes non renseignées, passez en mode avancé',
    },

    # translations by User:Uziel302, User:Uzielbot and User:Amire80, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Hebrew
    'he': {
        'create': 'יצירה',
        'csrf_warning': 'סליחה, לא יכולנו לעבד את הבקשה, האימות נכשל',
        'duplicates_warning': 'ליחידות המילוניות הקיימות הבאות יש אותו משפט מוגדר ואותו קוד שפה כמו למילה שאתם מנסים ליצור',
        'duplicates_instructions': 'אם אתם בטוחים שהם שונים, בדקו את התיבה בתחתית העמוד.',
        'no_duplicate': 'זה לא כפילות של יחידה מילונית קיימת.',
        'advanced': 'מתקדם',
        'advanced_general': 'אתם במצב מתקדם',
        'advanced_lexeme_id': 'ניתן להזין מזהה יחידה מילונית כדי להוסיף צורות ליחידה מילונית קיימת במקום ליצור אחת חדשה. השאירו צורות שכבר קיימות ביחידה מילונית ריקות, אחרת הן תוכפלנה!',
        'advanced_partial_forms': 'ניתן להשאיר צורות ריקות כך שלא תתווספנה. נא לוודא שלא השמטתם צורות כלשהן!',
        'lexeme_id': 'מזהה יחידה מילונית',
        'advanced_partial_forms_hint': 'לעדכון יחידות מילוניות שחסרות בהן צורות, יש לעבור למצב מתקדם',
        'generated_via': 'נוצר באמצעות',
        'bulk_link': 'מצב סיטונאי',
        'bulk_button': 'מצב סיטונאי',
        'bulk_heading': 'מצב סיטונאי',
        'bulk_format_help': 'עזרה בתסדיר',
        'bulk_not_allowed': 'אינ לך הרשאה להשתמש במצב סיטונאי. סליחה.',
        'edit_button': 'עריכה',
        'edit_link': 'עריכה',
        'edit_general': 'אתם במצב "עריכה". שינוי הערכים להלן יערוך, יוסיף, או יסיר צורות של היחידה המילונית המיועדת.',
        'edit_mismatch_warning': 'נראה שהיחידה המילונית הזאת אינה מתאימה לתבנית הזאת! נא לוודא שוב שזאת התבנית הנכונה ליחידה המילונית הזאת לפני המשך.',
        # note: the "two" and "many" tags are copied from the "other" tag
        'edit_ambiguous_warning': '{forms!p:one=צורת היחידה המילונית הבאה התאימה:two=צורות היחידה המילונית הבאות התאימו:many=צורות היחידה המילונית הבאות התאימו:other=צורות היחידה המילונית הבאות התאימו} ליותר מתבנית אחת באותו אופן:',
        'edit_unmatched_warning': '{forms!p:one=צורת היחידה המילונית הבאה לא התאימה:two=צורות היחידה המילונית הבאות לא התאימו:many=צורות היחידה המילונית הבאות לא התאימו:other=צורות היחידה המילונית הבאות לא התאימו} לאף אחת מהתבניות:',
        'edit_form_list_item': '{form_link}, {grammatical_feature_labels!l}, {statements!p:0=אין קביעות:one=קביעה אחת:two={statements} קביעות:many={statements} קביעות:other={statements} קביעות}',
        'no_grammatical_features': 'אין מאפיינים דקדוקיים',
    },

    # translations by User:Emptyfear and User:Kareyac, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Armenian
    'hy': {
        'create': 'Ստեղծել',
        'csrf_warning': 'Ցավոք, հարցումը հնարավոր չէ իրականացնել (<abbr title="Cross-site request forgery">CSRF</abbr> պաշտպանությունը ձախողվեց)։ Փորձեք ձևաթուղթը կրկին պահպանել։',
        'duplicates_warning': 'Հետևյալ բառույթներն ունեն նույն լեման և լեզվական կոդը, որոնք դուք ցանկանում եք ստեղծել:',
        'duplicates_instructions': 'Եթե համոզված եք, որ դրանք տարբեր են՝ տես ձևաթղթի ներքևի նշասալիկը։',
        'no_duplicate': 'Սա առկա լեմայի կրկնօրինակ չէ։',
        'advanced': 'Ընդլայնված',
        'advanced_general': 'Դուք ընդլայնված տարբերակում եք',
        'advanced_lexeme_id': 'Նոր բառույթ ստեղծելու փոխարեն՝ կարող եք ID֊ն նշել՝ արդեն գոյություն ունեցող բառույթին ձևեր ավելացնելու համար։ Արդեն գոյություն ունեցող բառույթի ձևերը դատարկ թողեք, թե չէ կկրկնօրինակվեն։',
        'advanced_partial_forms': 'Դուք կարող եք որոշ ձևեր դատարկ թողնել․ դրանք չեն ավելացվի։',
        'lexeme_id': 'Բառույթի ID',
        'advanced_partial_forms_hint': 'Որոշ ձևերի բացակայությամբ բառույթներ ստեղծելու համար՝ գնացեք ընդլայնված տարբերակ։',
        'edit_button': 'Խմբագրել',
        'edit_link': 'խմբագրել',
    },

    # translations by User:Sannita, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Italian
    'it': {
        'create': 'Crea il lessema!',
        'csrf_warning': 'Ops, non è possibile salvare la pagina (errore: <abbr title="Cross-site request forgery">CSRF</abbr> protection failed). Per favore, riprova.',
        'duplicates_warning': 'Attenzione, i seguenti lessemi hanno lo stesso lemma e codice linguistico di quello che hai appena tentato di creare:',
        'duplicates_instructions': 'Se sei sicuro che siano diversi, spunta la casella alla fine di questo modulo.',
        'no_duplicate': 'Questo NON è un duplicato di un lessema esistente.',
        'advanced': 'Avanzate',
        'advanced_general': 'Ti trovi nella modalità “avanzata”.',
        'advanced_lexeme_id': 'Puoi inserire un ID di un lessema esistente per aggiungere le forme mancanti, anziché crearne uno nuovo. NON inserire le forme già esistenti, altrimenti creerai un doppione!',
        'advanced_partial_forms': 'Se lasci un campo vuoto, non verrà creata nessuna forma. Assicurati di creare tutte le forme necessarie!',
        'lexeme_id': 'identificatore',
        'advanced_partial_forms_hint': 'Se vuoi creare dei lessemi privi di alcune forme, passa alla modalità avanzata.',
        'generated_via': 'generato tramite',
        'description_with_forms_and_senses': '{description}, {forms!p:0=nessuna forma:one=una forma:other={forms} forme} e {senses!p:0=nessun senso:one=un senso:other={senses} sensi}',
        'bulk_link': 'caricamento di massa',
        'bulk_button': 'Caricamento di massa',
        'bulk_heading': 'caricamento di massa',
        'bulk_format_help': 'aiuto formattazione',
        'bulk_not_allowed': 'Ci dispiace, ma non sei {user!g:m=autorizzato:f=autorizzata:n=autorizzato/a} a usare il caricamento di massa.',
        'edit_button': 'Modifica',
        'edit_link': 'modifica',
        'edit_general': 'Ti trovi nella modalità “modifica”. Cambia uno dei valori per modificare, aggiungere o rimuovere forme dal lessema.',
        'edit_mismatch_warning': 'Questo lessema non combacia con questo template! Per favore, controlla che questo sia il giusto template per il lessema prima di continuare.',
        'edit_ambiguous_warning': '{forms!p:one=La seguente forma:other=Le seguenti forme} del lessema combaciano con più di una forma nel template:',
        'edit_unmatched_warning': '{forms!p:one=La seguente forma:other=Le seguenti forme} del lessema non combaciano con alcuna delle forme nel template:',
        'edit_form_list_item': '{form_link}, {grammatical_feature_labels!l}, {statements!p:0=nessuna dichiarazione:one=una dichiarazione:other={statements} dichiarazioni}',
        'no_grammatical_features': 'nessuna caratteristica grammaticale',
    },

    # translations by User:Şêr, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Kurdish_(Kurmancî)
    'ku': {
        'create': '    Biafirîne',
        'csrf_warning': 'Bibore, me nikarî daxwaza te pêk bînin (bixebitînin) (Parastina <abbr title="Cross-site request forgery">CSRF</abbr>ê bi ser neket). Ji kerema xwe careke din hewl bide û formê dîsa bişîne.',
        'duplicates_warning': '    Ev leksem xwediyê heman peyv û heman koda zimanî ye, wek ya ku niha dixwazî biafirînî:',
        'duplicates_instructions': '    Ku tu bawer bî ku ev leksem ji hev cuda ne, ji kerema xwe re qutiya biçûk a di dawiya formê de nîşan bike.',
        'no_duplicate': '    Ev ne dubareya leksema heye ye.',
        'advanced': '    Pêşketî',
        'advanced_general': '    Tu di beşa rewşa "pêşketî" de yî.',
        'advanced_lexeme_id': '    Di şûna çêkirina leksemeke nû de, tu dikarî IDya leksemeke/bêjeyeke heye binivîsî ji bo lêzêdekirina forman li leksemeke heye. Ji kerema ma wan beşên ku di leksema heye de vala bihêle, da ku ev dubare neyên lêzêdekirin!',
        'advanced_partial_forms': '    Tu dikarî hin forman vala bihêlî, da ku ev lê zêde nebin. Lê hay jê hebe ku tu hin forman bi şaşî/xeletî ji bîr nekî (jê nebî)!',
        'lexeme_id': '    Lexem-ID',
        'advanced_partial_forms_hint': '    Ji bo çêkirina leksemên/bêjeyên nû derbasî rewşa pêşketî bibe.',
        'generated_via': '    hat çêkirin bi alîkariya',
        'description_with_forms_and_senses': '{description}, {forms!p:0=form tune ne:one=formek:other={forms} form} û {senses!p:0=bê wate:one=wateyek:other={senses} wate}',
    },

    # translations by Lucas Werkmeister
    'la': {
        'create': 'Facere',
        'csrf_warning': 'Excusa, error accidit. Quaeso, repete.',
        'duplicates_warning': '{lexemes!p:one=Sequens verbum:other=Sequentia verba} aequum lemma aequa linguaque {lexemes!p:one=habet:other=habent}:',
        'duplicates_instructions': 'Si certus es {lexemes!p:one=differens est:other=differentes sunt}, designa sic conclusio paginae.',
        'no_duplicate': 'Non duplex verbi existendi est.',
        'advanced': 'Modus amplificatus',
        'advanced_general': 'In modo amplificatum es.',
        'advanced_lexeme_id': 'Posses significare numerum verbi, ut formae ad id verbum addentur. Amitte formas qui id verbo exstant aut duplicis formas facies!',
        'advanced_partial_forms': 'Posses omittere aliqui formas, ut non addentur. Cave erroribus!',
        'lexeme_id': 'Numerus verbi',
        'advanced_partial_forms_hint': 'Ut facere verbi quae aliqui formas desunt, adi modo amplificatum.',
        'edit_button': 'Corrigere',
        'edit_link': 'corrigere',
        'edit_general': 'In modo corrigendi es. Sic mutas scriptum inferum, formas verbi mutabuntur, addentur vel removebuntur.',
    },

    # translations by User:Jsamwrites, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Malayalam
    'ml': {
        'create': 'സൃഷ്ടിക്കുക',
        'csrf_warning': 'ക്ഷമിക്കണം, ഞങ്ങൾക്ക് ഈ അഭ്യർത്ഥന പ്രോസസ്സ് ചെയ്യാൻ കഴിഞ്ഞില്ല (<abbr title="ക്രോസ്-സൈറ്റ് വ്യാജ അഭ്യർത്ഥന">CSRF</abbr> പരിരക്ഷണം പരാജയപ്പെട്ടു). ഫോം വീണ്ടും സമർപ്പിക്കാൻ ശ്രമിക്കുക.',
        'duplicates_warning': 'നിങ്ങൾ സൃഷ്ടിക്കാൻ ശ്രമിക്കുന്ന താഴെ കൊടുത്തിരിക്കുന്ന ലെക്സീമുകൾക്ക് അതേ ലെമ്മയും ഭാഷാ കോഡും ഉണ്ട്',
        'duplicates_instructions': 'അവ വ്യത്യസ്തമാണെന്ന് നിങ്ങൾക്ക് ഉറപ്പുണ്ടെങ്കിൽ, ഫോമിന്റെ ചുവടെയുള്ള ബോക്സ് ചെക്കുചെയ്യുക.',
        'no_duplicate': 'ഇത് നിലവിലുള്ള ലെക്സീമിന്റെ തനിപ്പകർപ്പല്ല.',
        'advanced': 'വിപുലമായ മോഡ്',
        'advanced_general': 'നിങ്ങൾ “വിപുലമായ” മോഡിലാണ്.',
        'advanced_lexeme_id': 'പുതിയൊരെണ്ണം സൃഷ്ടിക്കുന്നതിനുപകരം നിലവിലുള്ള ഒരു ലെക്സീമിലേക്ക് ഫോമുകൾ ചേർക്കാൻ നിങ്ങൾക്ക് ഒരു ലെക്സീം ഐഡന്റിഫയർ നൽകാം. ലെക്സീമിൽ നിലവിലുള്ള ഏതെങ്കിലും ഫോമുകൾ ശൂന്യമായി വിടുക, അല്ലാത്തപക്ഷം അവ തനിപ്പകർപ്പാകും!',
        'advanced_partial_forms': 'നിങ്ങൾ ചില ഫോമുകൾ ശൂന്യമാക്കിയിടുകയാണെങ്കിൽ, അവ ചേർക്കില്ല. നിങ്ങൾ യാദൃശ്ചികമായി ഏതെങ്കിലും ഫോമുകൾ ഉപേക്ഷിക്കുന്നില്ലെന്ന് ഉറപ്പാക്കുകe',
        'lexeme_id': 'ലെക്സീം ഐഡന്റിഫയർ',
        'advanced_partial_forms_hint': 'ശൂന്യമായ ചില ഫോമുകൾ ഉപയോഗിച്ച് ലെക്സീമുകൾ സൃഷ്ടിക്കാൻ, വിപുലമായ മോഡിലേക്ക് മാറുക.',
        'generated_via': 'ഉപയോഗിച്ച് ജനറേറ്റുചെയ്തു',
        'bulk_link': 'ബൾക്ക് മോഡ്',
        'bulk_button': 'ബൾക്ക് മോഡ്',
        'bulk_heading': 'ബൾക്ക് മോഡ്',
        'bulk_format_help': 'ഫോർമാറ്റ് മനസിലാക്കുന്നതിനുള്ള മാനുവൽ',
        'bulk_not_allowed': 'ബൾക്ക് മോഡ് ഉപയോഗിക്കാൻ നിങ്ങൾക്ക് അനുവാദമില്ല. ക്ഷമിക്കണം.',
    },

    # translations by User:Danmichaelo and User:Jon Harald Søby, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Norwegian_Bokmål
    'nb': {
        'create': 'Opprett',
        'csrf_warning': 'Forespørselen din ble ikke behandlet på grunn av et <abbr title="Cross-site request forgery">CSRF</abbr>-problem. Prøv gjerne om igjen.',
        'duplicates_warning': 'Følgende eksisterende leksemer har samme lemma og språkkode som de du holder på å opprette:',
        'duplicates_instructions': 'Hvis du er sikker på at de er ulike kan du hake av i avkrysningsboksen i skjemaet.',
        'no_duplicate': 'Dette er ikke et duplikat av et leksem som finnes fra før.',
        'advanced': 'Avansert',
        'advanced_general': 'Du er i avansert modus.',
        'advanced_lexeme_id': 'Du kan skrive inn ID-en til et leksem som allerede finnes i stedet for å opprette et nytt. La alle formene som allerede er lagt inn stå tomme, ellers blir de duplisert!',
        'advanced_partial_forms': 'Du kan la noen felt stå tomme slik at de ikke blir lagt til, men pass på at du ikke glemmer å fylle inn noen av formene som skal være med.',
        'lexeme_id': 'Leksem-ID',
        'advanced_partial_forms_hint': 'Bytt til avansert modus om du ønsker å opprette leksemer uten alle formene.',
        'generated_via': 'generert via',
        'description_with_forms_and_senses': '{description}, {forms!p:0=ingen former:one=én form:other={forms} former} og {senses!p:0=ingen betydninger:one=én betydning:other={senses} betydninger}',
        'bulk_link': 'masseinnleggingsmodus',
        'bulk_button': 'Masseinnleggingsmodus',
        'bulk_heading': 'masseinnleggingsmodus',
        'bulk_format_help': 'formathjelp',
        'bulk_not_allowed': 'Du har dessverre ikke tillatelse til å bruke masseinnleggingsmodus.',
        'edit_button': 'Rediger',
        'edit_link': 'rediger',
        'edit_general': 'Du er i redigeringsmodus. Hvis du endrer verdiene nedenfor blir målleksemet redigert.',
        'edit_mismatch_warning': 'Dette leksemet passer ikke med denne malen! Dobbeltsjekk at det er riktig mal for dette leksemet før du fortsetter.',
        'edit_ambiguous_warning': '{forms!p:one=Denne leksemformen:other=Følgende leksemformer} matchet mer enn ett malskjema like godt:',
        'edit_unmatched_warning': '{forms!p:one=Denne leksemformen:other=Følgende leksemformer} matchet ikke noen av malskjemaene:',
        'edit_form_list_item': '{form_link}, {grammatical_feature_labels!l}, {statements!p:0=ingen påstander:one=én påstand:other={statements} påstander}',
        'no_grammatical_features': 'ingen grammatiske trekk',
    },

    # translations by User:MarcoSwart, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Dutch
    'nl': {
        'create': 'Aanmaken',
        'csrf_warning': 'Sorry, we konden dit niet verwerken (door de <abbr title="Cross-site request forgery">CSRF</abbr>-bescherming). Probeer het webformulier nog eens aan te bieden.',
        'duplicates_warning': 'Je probeert een lexeem aan te maken met hetzelfde lemmawoord en taalcode als een of meer bestaande lexemen:',
        'duplicates_instructions': 'Weet je zeker dat je echt iets anders aanmaakt? Kruis dan het vakje voor de laatste regel aan.',
        'no_duplicate': 'Dit is geen doublure van een lexeem dat al bestaat.',
        'advanced': 'Geavanceerd',
        'advanced_general': 'Geavanceerde mogelijkheden.',
        'advanced_lexeme_id': 'Vul een lexeem ID in om woordvormen aan een bestaand lexeem toe te voegen. Woordvormen die het lexeem al heeft hier niet invullen, want dat geeft een doublure.',
        'advanced_partial_forms': 'Als je woordvormen niet invult, worden ze niet toegevoegd. Let op dat je niet per ongeluk een woordvorm vergeet!',
        'lexeme_id': 'Lexeem-ID',
        'advanced_partial_forms_hint': 'Ga naar "Geavanceerd" als je een lexeem wil maken waarin een of meer woordvormen ontbreken.',
        'generated_via': 'gegenereerd door',
    },

    # translations by User:Njardarlogar, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Norwegian_Nynorsk
    'nn': {
        'create': 'Opprett',
        'csrf_warning': 'Førespurnaden kunne ikkje handsamast av di <abbr title="Cross-site request forgery">CSRF</abbr>-vernet mislukkast. Freist gjerne om att.',
        'duplicates_warning': 'Desse leksema finst frå før og har det samme lemmaet og den same språkkoden som leksemet du held på å oppretta.',
        'duplicates_instructions': 'Om du er viss på at dei er ulike, hak av boksen på botnen av skjemaet.',
        'no_duplicate': 'Dette er ikkje eit duplikat av eit leksem som finst frå før.',
        'advanced': 'Avansert',
        'advanced_general': 'Du er i avansert modus.',
        'advanced_lexeme_id': 'Du kan skriva inn ID-en til eit leksem som alt finst i staden for å oppretta eit nytt eit. La alle formene som alt er opppførte på leksemsida vera tomme, elles vert dei dupliserte.',
        'advanced_partial_forms': 'Du kan la nokre felt vera tomme slik at dei ikkje vert lagde til. Gjer deg viss på at du ikkje gløymer å skriva inn nokre av formene som skal vera med.',
        'lexeme_id': 'Leksem-ID',
    },

    # translations by User:KaMan, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Polish
    'pl': {
        'create': 'Utwórz',
        'csrf_warning': 'Niestety przetworzenie tego żądania było niemożliwe (ochrona <abbr title="Cross-site request forgery">CSRF</abbr>). Proszę spróbować przesłać formularz ponownie.',
        'duplicates_warning': 'Następujące istniejące leksemy mają tę samą formę kanoniczną i kod języka jak ten, który próbujesz utworzyć:',
        'duplicates_instructions': 'Jeśli masz pewność, że one są różne, zaznacz kratkę u dołu formularza.',
        'no_duplicate': 'To nie jest duplikat istniejącego leksemu.',
        'advanced': 'Zaawansowane',
        'advanced_general': 'Jesteś w trybie “zaawansowanym”.',
        'advanced_lexeme_id': 'Możesz podać ID leksemu by dodać formy do istniejącego leksemu, zamiast tworzyć nowy leksem. Formy, które już istnieją, pozostaw puste, w przeciwnym wypadku zostaną one powielone!',
        'advanced_partial_forms': 'Możesz zostawić niektóre formy puste, dzięki czemu nie zostaną one dodane. Upewnij się, że przypadkowo nie pominąłeś żadnej formy!',
        'lexeme_id': 'ID leksemu',
        'advanced_partial_forms_hint': 'Aby utworzyć leksemy z pominięciem niektórych form, przełącz się na tryb zaawansowany.',
        'generated_via': 'wygenerowane przez',
    },

    # translations by User:Ederporto and Lucas Werkmeister, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Portuguese
    'pt': {
        'create': 'Criar',
        'csrf_warning': 'Desculpe, não foi possível processar essa requisição (proteção contra <abbr title="Cross-site request forgery">CSRF</abbr> falhou). Por favor, tente submeter o formulário novamente.',
        'duplicates_warning': 'Os seguintes lexemas têm o mesmo lema e código de língua que o lema que você está tentando criar:',
        'duplicates_instructions': 'Se você tem certeza que eles são diferentes, selecione a caixa no final do formulário.',
        'no_duplicate': 'Isto não é uma duplicata de um lexema existente.',
        'advanced': 'Avançado',
        'advanced_general': 'Você está no modo «Avançado».',
        'advanced_lexeme_id': 'No lugar de criar um novo lexema, você pode adicionar um identificador de um lexema existente para adicionar as formas faltantes. Deixe em branco as formas já existentes no lexema; Do contrário, será criada uma duplicata!',
        'advanced_partial_forms': 'Você pode deixar algumas formas vazias para evitar que sejam adicionadas. Garanta criar todas as formas necessárias!',
        'lexeme_id': 'Identificador de lexema',
        'advanced_partial_forms_hint': 'Para criar lexemas com algumas formas faltando, mude para o modo avançado.',
        'generated_via': 'gerado via',
    },

    # translations by User:Infovarius and User:Amire80, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Russian
    'ru': {
        'create': 'Создать',
        'csrf_warning': 'Извините, запрос не получился (<abbr title="Cross-site request forgery">CSRF</abbr> ошибка защиты). Пожалуйста, попробуйте отправить форму снова.',
        'duplicates_warning': 'Следующие лексемы имеют такие же лемму и язык, что и создаваемая вами:',
        'duplicates_instructions': 'Если вы уверены, что они отличаются, отметьте галочкой внизу формы.',
        'no_duplicate': 'Это не дубликат существующей лексемы',
        'advanced': 'Расширенные настройки',
        'advanced_general': 'Вы в “продвинутом” режиме.',
        'advanced_lexeme_id': 'Вы можете ввести ID лексемы, чтобы добавить формы в неё вместо создания новой лексемы. Оставьте формы, которые уже существуют, незаполненными, иначе они будут добавлены повторно!',
        'advanced_partial_forms': 'Вы можете оставить некоторые формы пустыми, чтобы они не были добавлены. Убедитесь, что вы не сделали этого случайно!',
        'lexeme_id': 'ID лексемы',
        'advanced_partial_forms_hint': 'Чтобы создать лексемы без некоторых форм, переключитесь в продвинутый режим.',
        'generated_via': 'сгенерировано с помощью',
        'description_with_forms_and_senses': '{description}, {forms!p:0=нет форм:one=одна форма:few={forms} формы:many={forms} форм:other={forms} формы} и {senses!p:0=нет значений:one=одно значение:few={senses} значения:many={senses} значений:other={senses} значения}',
    },

    # translations by User:Vesihiisi, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Swedish
    'sv': {
        'create': 'Skapa',
        'csrf_warning': 'Din begäran kunde inte utföras på grund av ett <abbr title="Cross-site request forgery">CSRF</abbr>-fel. Var god försök igen.',
        'duplicates_warning': 'Dessa befintliga lexem har samma lemma och språkkod som lexemet du försöker skapa:',
        'duplicates_instructions': 'Om du är säker på att de är olika, markera i kryssrutan längst ner i formuläret.',
        'no_duplicate': 'Duplicerar ej ett befintligt lexem.',
        'advanced': 'Avancerat läge',
        'advanced_general': 'Du är nu i avancerat läge',
        'advanced_lexeme_id': 'Här kan du skriva in ett lexem-ID för att lägga till former till ett befintligt lexem istället för att skapa ett nytt. För att undvika att redan befintliga former dupliceras, lämna dessa fält tomma.',
        'advanced_partial_forms': 'Du kan lämna vissa fält tomma; dessa former kommer då inte att läggas till. Försäkra dig dock om att du inte lämnar några fält tomma av misstag!',
        'lexeme_id': 'Lexem-ID',
        'advanced_partial_forms_hint': 'För att skapa lexem utan att fylla i alla fält, byt till avancerat läge.',
        'bulk_link': 'masskapa',
        'bulk_button': 'Masskapa',
        'bulk_heading': 'masskapa',
        'bulk_format_help': 'formateringshjälp',
        'bulk_not_allowed': 'Du får dessvärre inte masskapa lexem.',
    },

    # translations by User:Info-farmer, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Tamil
    'ta': {
        'create': 'உருவாக்குக',
        'csrf_warning': 'மன்னிக்க, தற்போது இவ்வேண்டுகோளை எங்களால் நடைமுறைசெய் இயலாது(<abbr title="Cross-site request forgery">CSRF</abbr> பாதுகாப்புத் தோல்வி) எனவே, மீண்டும் உள்ளீடுகளைத் தருக.',
        'duplicates_warning': 'கீழ்கண்ட சொற்பொருளன்கள், நீங்கள் உருவாக்கும் மொழியில் ஏற்கனவே உள்ளன:',
        'duplicates_instructions': 'இச்சொற்பொருளன்கள் வேறுபட்ட வடிவமெனில், இப்படிவத்தின் அடியிலுள்ள சிறுகட்டத்தினைத் தெரிவு செய்க',
        'no_duplicate': 'இது ஏற்கனவே உள்ள சொற்பொருளனின், அதே இலக்கண வடிவமல்ல.',
        'advanced': 'மேம்பட்டது',
        'advanced_general': '“மேம்பட்ட இயக்கமுறை தோற்றத்தில்” உள்ளீர்கள்.',
        'advanced_lexeme_id': 'புதிய சொற்பொருளனை உருவாக்குவதற்கு பதிலாக, ஏற்கனவே உள்ள சொற்பொருளனின் குறியீட்டைக் குறித்து, அச்சொற்பொருளனின் வடிவங்களைச் சேர்க்கலாம். சொற்பொருளனில் ஏற்கனவே உள்ள வடிவத்தினை வெற்றாக விட்டால், இதே இலக்கண வடிவங்கள் தோன்றாது.',
        'advanced_partial_forms': 'நீங்கள் சில வடிவங்களை வெற்றாக விட்டுவிட்டால், அவை இணையாது. இருப்பினும், தவறுதலாக எவ்வடிவங்களையும் விட்டுவிடாமல் பார்த்துக் கொள்ளுங்கள்!',
        'lexeme_id': 'சொற்பொருளனின் குறியீடு',
        'advanced_partial_forms_hint': 'சில வடிவங்களைத் தவிர்த்த, சொற்பொருளன்களை உருவாக்க, மேம்பட்ட இயக்கமுறைக்கு மாறுக.',
    },

    # translations by User:Tohaomg, see https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms/Ukrainian
    'uk': {
        'create': 'Створити',
        'csrf_warning': 'Вибачте, не вийшло обробити цей запит (помилка системи захисту <abbr title="Cross-site request forgery">CSRF</abbr>). Будь ласка, спробуйте відіслати форму ще раз.',
        'duplicates_warning': 'Наступні вже існуючі лексеми мають такі самі лему та мову, що і лексема яку ви намагаєтесь створити:',
        'duplicates_instructions': 'Якщо ви впевнені що це мають бути дві різні лексеми, поставте галочку внизу форми.',
        'no_duplicate': 'Це не дублікат існуючої лексеми.',
        'advanced': 'Розширені налаштування',
        'advanced_general': 'Ви перебуваєте в режимі розширених налаштувань.',
        'advanced_lexeme_id': 'Ви можете ввести ID вже існуючої лексеми, щоб додати форми до неї замість створення нової лексеми. Залиште форми, які вже існують в лексемі, порожніми, інакше вони будуть додані повторно!',
        'advanced_partial_forms': 'Ви можете залишити деякі форми порожніми, щоб вони не були додані. Переконайтесь що не залишили порожніх форм випадково!',
        'lexeme_id': 'ID лексеми',
        'advanced_partial_forms_hint': 'Щоб створити лексему без деяких форм, переключіться в режим розширених налаштувань.',
    },

}


def initial_titlecase(s):
    return s[:1].title() + s[1:]


def identity(s):
    return s


variables = {
    'duplicates_warning': ['lexemes'],
    'duplicates_instructions': ['lexemes'],
    'description_with_forms_and_senses': ['description', 'forms', 'senses'],
    'bulk_not_allowed': ['user'],
    'edit_ambiguous_warning': ['forms'],
    'edit_unmatched_warning': ['forms'],
    'edit_form_list_item': ['form_link', 'grammatical_feature_labels', 'statements'],
}
lists = {
    'edit_form_list_item': {'grammatical_feature_labels'},
}
derived_messages = {
    'bulk_button': ('bulk_link', initial_titlecase),
    'bulk_heading': ('bulk_link', identity),
    'edit_button': ('edit_link', initial_titlecase),
}


def py2mw(py, variables, lists):
    def replace(match):
        nonlocal variables, lists
        inner = match[0][1:-1] # strip away braces
        variable, _, rest = inner.partition('!')
        number = variables.index(variable) + 1
        if not rest:
            return f'${number}'
        conversion, _, format_spec = rest.partition(':')
        format_spec = format_spec.replace('{' + variable + '}', f'${number}')
        if conversion == 'p':
            args = []
            for plural in format_spec.split(':'):
                key, _, text = plural.partition('=')
                if key.isnumeric():
                    args.append(plural)
                else:
                    args.append(text)
            return '{{PLURAL:$' + str(number) + '|' + '|'.join(args) + '}}'
        elif conversion == 'g':
            args = []
            for replacement in format_spec.split(':'):
                gender, _, text = replacement.partition('=')
                args.append(text)
            return '{{GENDER:$' + str(number) + '|' + '|'.join(args) + '}}'
        elif conversion == 'l':
            assert variable in lists
            return f'${number}'
        else:
            raise ValueError(f'Unknown conversion {conversion}')
    return re.sub(r'\{([^{}]|\{[^}]*\})*\}', replace, py)


if __name__ == '__main__':
    for language in translations:
        with open(f'i18n/{language}.json', 'w') as f:
            data = {}
            for key in translations[language]:
                if key in derived_messages:
                    source_key, transformation = derived_messages[key]
                    assert translations[language][key] == transformation(translations[language][source_key])
                else:
                    msg = py2mw(translations[language][key], variables.get(key, []), lists.get(key, set()))
                    data[key] = msg
            json.dump(data, f, ensure_ascii=False, indent='\t')
            f.write('\n')
