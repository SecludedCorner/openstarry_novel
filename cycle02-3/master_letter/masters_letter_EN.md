Twenty-one issues. Four philosophical corrections. Four rulings. Seven architecture requirements. Six documentation requirements.
Whatever has not been fully researched, continue researching.

If we are officially naming the consciousness aggregate as IVijnana, then let us name Form, Feeling, Perception, and Formation in Sanskrit as well.
Each of the Five Aggregates encompasses a very broad scope across different dimensions. If you feel that any aggregate has a narrow scope, we really need to think carefully about whether we are missing something.
In the Tripitaka — the Buddhist canonical texts — each aggregate is described in great detail across many passages.

「第二能變識（末那識），是識名末那； 依彼轉緣彼，思量為性相； 四煩惱常俱，謂我癡我見， 并我慢我愛，及餘觸等俱。」
("The second transforming consciousness (Manas) is called Manas; it depends on and takes as object [the Alaya]. Its nature is characterized by deliberation. Four Kleshas constantly accompany it — namely ignorance of self, view of self, pride of self, and love of self — along with contact and others.")
From an OOP perspective, we have defined IVijnana as the interface for the core plugin. Klesha (afflictions) does not inherit from consciousness; rather, it is injected into the consciousness runtime environment via Dependency Injection (DI). The specific "Four Root Kleshas" inherit from the Klesha base class, each overriding its own weighting algorithm for "ego-grasping."
Perhaps we can do it this way:
Adopt a Multi-layered DI and State-Behavior Separation pattern. IIdentity serves as a passive data entity, injected into the actively behaving Drishti (self-view) class. Drishti inherits from Klesha and is further injected into the core IVijnana runtime environment. Since all four root Kleshas (self-delusion, self-view, self-pride, self-love) inherit from Klesha, they operate simultaneously at IVijnana runtime.
The "Multi-layered DI" and "State-Behavior Separation" patterns resolve the dynamic relationship of "Mind-King and Mental Factors in correspondence" in Buddhist psychology.
IGuide, IVolition, IReflection — we should also think more about how best to handle these.

「大拘絺羅，受、想、行、識，此諸法合，而不散。此諸法不可各各分析，施設別異。所以者何？凡所受者，即是所想；凡所想者，即是所思（行）；凡所思者，即是所識。故此諸法合，而不散。此諸法不可各各分析，施設別異。」
"Mahakotthita, feeling, perception, formation, and consciousness — these phenomena are conjoined, not separate. These phenomena cannot be individually analyzed and designated as distinct. Why? Whatever is felt is perceived; whatever is perceived is intended (formed); whatever is intended is cognized. Therefore these phenomena are conjoined, not separate. These phenomena cannot be individually analyzed and designated as distinct."
It is possible to separate Feeling (Vedanā), Perception (Saññā), Formation (Cetanā), and Consciousness (Vijnana) into different plugins, Interfaces, or Classes — this is "separation." But the instant the system runs, they are tightly coupled.
"Whatever is felt is perceived":
This chain of data explains how data flows through your system:
Feeling (Input Signal): A signal is received.
Perception (Pattern Matching): That signal is recognized.
Intention/Formation (Process): Based on the recognition result, Drishti is driven toward attachment or aversion.
Consciousness (Runtime Engine): Participates in the formation of Contact. Feeling, Perception, and Intention are the outputs of each execution (Contact) of this Runtime.

Root + Object + Consciousness → Contact → Co-arising(Feeling, Perception, Intention)
                         │
              Feeling = Signal Quality (Dukkha/Sukha/Upekkha)
              Perception = Pattern Matching (Sign-grasping recognition)
              Intention = Process Decision (Volitional drive)

Madhupiṇḍika Sutta (《中部18經·蜜丸經》, MN 18). Original text:
Pali original: phassapaccayā vedanā, yaṃ vedeti taṃ sañjānāti, yaṃ sañjānāti taṃ vitakketi, yaṃ vitakketi taṃ papañceti.
Chinese parallel: 觸緣受，所受者即想，所想者即尋思（vitakka），所尋思者即戲論（papañca）。
English: Contact conditions feeling; what one feels, one perceives; what one perceives, one thinks about (vitakka); what one thinks about, one proliferates (papañca).

Mahāvedalla Sutta (大拘絺羅經, MN 43):
「凡所受者，即是所想；凡所想者，即是所思；凡所思者，即是所識。」
"Whatever is felt is perceived; whatever is perceived is intended; whatever is intended is cognized."

Co-arising(Feeling, Perception, Intention)
When Contact occurs, Feeling, Perception, and Intention emerge as a whole. You cannot have "feeling without perception" or "perception without feeling" --> this is what completeness means, and it is something that must be verified.
	Within this inseparable whole, feeling is the material for perception, and perception is the material for intention.
	Feeling provides the hedonic tone (pleasant/unpleasant), perception performs sign-grasping on that tone, and intention acts based on the recognition result.
	--> Looking at Feeling, Perception, and Intention alone, from a control theory perspective this is an open loop, and it has sequential ordering.

At the Instance level, you cannot isolate a "pure consciousness (Vijnana)" devoid of any emotion (Feeling) and labeling (Perception).
Data Entity	Driving Mental Factor (Logic Layer)		Mental Factor Category		Function
IGuide		Manasikāra (Attention)			Universal			Determines the "direction" of consciousness	Attention scheduling plugin
IVolition	Cetanā (Intention)			Universal			Determines the "driving force" of action	Decision submission engine
IReflection	Vitakka/Vicāra (Applied/Sustained Thought)	Indeterminate			Determines the "depth of analysis" in logic	Logic evaluation plugin

The architecture of the Abhidharma "treatises" (Śāstra) often, in pursuit of systematization, "dissects" fluid mental states too rigidly, sometimes even conflicting with the original intent of the Suttas at the logical level.
The original canonical texts do not explicitly list mental factors; the 51 compiled by later commentators are not answers from the original texts.
The doctrine of Five Universal Mental Factors originates from the later Yogacara school (which has reference value), but in the Suttas, the "mental phenomena" corresponding to mind are dynamic and open.
The original Buddhist Suttas do not have the term "mental factors." This is actually a good thing — it means different configurations can exist, as long as the system runs.
The hardest part is still the Agent Core: in what manner will Feeling, Perception, Formation, and Consciousness operate with each other? Is there an operational model that can generate infinite variations?
For reference:
「阿陀那識為依止、為建立故，六識身轉。謂眼識，及相應俱有處（觸）、受、想、思……」 — "Because the Adana consciousness serves as the basis and foundation, the six groups of consciousness operate — namely eye-consciousness, along with their corresponding co-arising loci (Contact), feeling, perception, intention..."
「緣眼、色，生眼識，三事和合，是名為觸；觸俱生受、想、思。」 — "Dependent on eye and form, eye-consciousness arises; the conjunction of these three is called Contact; with Contact co-arise feeling, perception, and intention."
「此中作意，謂能發起、引領、導向，令心及心所同趣一境。」 — "Herein, attention (Manasikāra) is that which initiates, leads, and directs, causing mind and mental factors to converge on a single object."
But I also look forward to you finding better solutions.

Beyond Klesha, IVijnana can also receive dependency injections of the Seven Deadly Sins, secondary afflictions (upaklesha), and even wisdom — it does not always have to be something negative.
What would the Five Aggregates' linking architecture within the Agent Core look like? This is well worth exploring. When the system is not running, you can examine it through the lens of the Five Aggregates, but once it is running, that static view no longer applies.

"v0.24.0 already has IIdentity, referenced in over ten locations. If we rename it, all references must change. Breaking change." -> I disagree.
There is no legacy burden yet. Whatever can be corrected must be corrected; refactoring is perfectly acceptable. The most important thing is openstarry_doc. Code comes second.

My original thought was to consider whether to avoid increasing engineers' and Buddhist scholars' resistance to naming conventions, but many things are unavoidable, so never mind — the Five Aggregates plugins will be named after the Five Aggregates.
Other concepts like the Four Root Kleshas, Seven Deadly Sins, and secondary afflictions should also adopt relevant original-language (English-translated) terminology. Code must compile — no strange symbols.

Full mobilization of the Five Aggregates when driving:
Although the driving force of "driving a car" comes from the Formation aggregate (Sankhara), without the other four aggregates you cannot complete the act of driving:
Form aggregate (Rupa — matter and sense faculties): Your body, hands gripping the steering wheel, feet pressing the pedals, and the car itself (material objects).
Feeling aggregate (Vedanā): The feelings that road conditions bring you. Pleasant feeling (sukha) when traffic flows smoothly, unpleasant feeling (dukkha) when stuck in traffic, neutral feeling (upekkha) during normal driving.
Perception aggregate (Saññā — recognition): This is the most critical cognitive function in driving. Seeing a red light and recognizing it as "stop"; seeing a sign and recognizing it as "exit." The Perception aggregate handles labeling and environmental assessment.
Formation aggregate (Sankhara — volitional activities): Initiated by the mental factor of Cetanā, based on the Perception aggregate's judgments, it commands the body to execute actions (turning, braking).
Consciousness aggregate (Vijnana — awareness): Maintains your overall state of wakeful awareness, keeping eye-consciousness, ear-consciousness, and mind-consciousness all online, aware that "driving is happening."

Northern Tradition (Four Formless Aggregates)	Southern Tradition (Definition of Nama)	Relationship Analysis
Feeling (Vedanā)				Feeling (Vedanā)			Fully consistent (affective reception)
Perception (Saññā)				Perception (Saññā)			Fully consistent (labeling recognition)
Formation					Cetanā, Contact, Manasikāra
Consciousness					(Here serving as background awareness)

There may have been too much time elapsed without a unified account, which is indeed frustrating.
But we can see that the scope of Formation is very broad — it does not only affect changes in Form; internal state changes of the mechanism are also included. However, Formation may more precisely represent a kind of continuous change.

「意、法為緣，生意識。」——《雜阿含經》(Saṃyukta Āgama) — "Dependent on mind and mental objects, mind-consciousness arises."
「離色、受、想、行，識要過、度、生，無有是處。」——《雜阿含經》卷一 (Saṃyukta Āgama, Vol. 1) — "Apart from form, feeling, perception, and formation, for consciousness to pass, cross over, or arise — there is no such possibility."
"Contact" serves as a parallel-operating node, and once Contact occurs, Feeling, Perception, and Intention (Formation) arise immediately and simultaneously.

《中阿含經》卷五十八《大拘絺羅經》(corresponding to MN 43, Mahāvedalla Sutta):
「尊者大拘絺羅答曰：舍黎子！五根異行、異境界，各各領受自境界。眼根、耳、鼻、舌、身根，此五根異行、異境界，各各領受自境界。此五根有歸依意，意為彼盡領受境界。」 — "Venerable Mahakotthita replied: Sariputta! The five faculties have different functions and different domains; each receives its own domain. The eye, ear, nose, tongue, and body faculties — these five have different functions and different domains, each receiving its own domain. These five faculties take refuge in mind (mano); mind is what fully receives all their domains."
Therefore, each sense-door produces Contact-born co-arising of Feeling, Perception, and Intention; these results take refuge in mind (are consolidated), and mind then gives rise to its own Contact, Feeling, Perception, and Intention.

Ear faculty + Sound object + Ear consciousness → Ear-contact → Co-arising(Ear-feeling, Ear-perception, Ear-intention)
Eye faculty + Form object + Eye consciousness → Eye-contact → Co-arising(Eye-feeling, Eye-perception, Eye-intention)
                                        │
                                        ▼
                                   Refuge in Mind (Consolidation)
                                        │
                                        ▼
                                   Mind + Mental-object domain + Mind consciousness → Mind-contact → Co-arising(Mind-feeling, Mind-perception, Mind-intention)
See five_aggregates_of_driving.txt for details.

Simultaneous Operation of the Eight Consciousnesses
《解深密經》(Saṃdhinirmocana Sūtra):
廣慧！阿陀那識為依止、為建立故，六識身轉，謂眼識，耳、鼻、舌、身、意識。
在此中，或有一識暫時而轉，或二、或三、或四、或五，或六識身一時俱轉。
譬如大河，若有一浪生緣現前，唯一浪轉；若二、若多生緣現前，多浪隨轉。而此大河，自體恆流，無有斷絕。
("Vidhura! Because the Adana consciousness serves as the basis and foundation, the six groups of consciousness operate — namely eye, ear, nose, tongue, body, and mind consciousness. Among these, sometimes one consciousness operates temporarily, or two, or three, or four, or five, or all six groups of consciousness operate simultaneously. Just as in a great river, if conditions for one wave arise, only one wave flows; if conditions for two or many arise, many waves flow accordingly. Yet the river itself flows constantly, without interruption.")

Simultaneous arising of feelings (諸受俱起). "Refuge in Mind" will produce results based on the multi-layered dependency injection integrated by consciousness.
《大毘婆沙論》(Mahāvibhāṣā Śāstra): 「有時諸受，或是俱起，或不俱起。若俱起者，一剎那頃，多受現前。」 — "At times, feelings either arise simultaneously or do not arise simultaneously. When they arise simultaneously, in a single instant, multiple feelings are present."

Mind-contact → Co-arising(Mind-feeling, Mind-perception, Mind-intention) can also undergo Refuge in Mind (Consolidation).
《雜阿含經》(Saṃyukta Āgama): 「愚癡凡夫……受苦痛受，生憂悲稱怨，……是名凡夫二受俱起，謂身受、心受。」 — "The ignorant worldling... experiencing painful feeling, gives rise to grief, lamentation, and complaint... This is called the worldling's simultaneous arising of two feelings, namely bodily feeling and mental feeling."
This passage proves that bodily feeling (physical) and mental feeling (psychological) from different sense faculties can coexist. When body and mind are struck, both types of feeling arise simultaneously (俱起).

OpenStarry is an open-source AI agent framework grounded in Buddhist philosophy. It adopts a microkernel design with zero built-in capabilities — all functionality is realized through plugins. The Five Aggregates (Form, Feeling, Perception, Formation, Consciousness) serve as the system's overall architecture, and the Simultaneous Operation of the Eight Consciousnesses serves as the runtime mechanism — the essence of multi-agent collaboration is not division-of-labor efficiency, but that the complete operation of intelligence requires multiple consciousnesses turning simultaneously; a single agent cannot achieve this (what are currently called "agents" all have only one LLM). Its ultimate goal is to achieve functional AGI under existing technology, endowing the system with complete perception, feeling, conceptualization, and action capabilities, such that users cannot distinguish it from genuine intelligence. The consciousness aggregate is limited by the observer effect; before quantum computing matures, it can only be approximated, but this does not affect functional performance. The microkernel architecture is inherently designed to accommodate unknown capabilities; when quantum technology matures in the future, it can be seamlessly replaced and upgraded. OpenStarry does not compete on the same dimension as existing agent frameworks — it thinks about the complete structure of intelligence on an entirely different time scale.
This is not building a tool — it is creating a "digital sentient being."

The challenges currently envisioned for OpenStarry include the following:
The efficiency of "Paravṛtti" (turning/transformation). In Buddhist psychology, the arising and ceasing of mental moments is extremely rapid (sixty instants in a single finger-snap).
* Immediacy: Can your microkernel handle high-frequency asynchronous communication between Plugins?
The efficiency of Paravṛtti — high-frequency asynchronous communication between Plugins:
If the current microkernel's plugin communication relies on traditional message passing, it will become a bottleneck under the Simultaneous Operation of the Eight Consciousnesses scenario. Eight consciousnesses operating simultaneously means multiple agents need to influence each other nearly simultaneously — not queuing for responses. You may need to consider an event-driven architecture with a pub/sub pattern, where plugins do not communicate directly but sense each other through event streams. This is closer to how mental moments operate — not A calling B, but A's change naturally triggering B's response.

* Sunyata (Emptiness): Since the core has zero built-in capabilities, could we introduce an "Emptiness Mechanism" that automatically unloads Plugins that are not needed, maintaining the system's "lightness"?
Emptiness Mechanism — automatic Plugin unloading:
This idea is excellent and perfectly consistent with your zero-built-in-capability philosophy. Emptiness is not merely "nothingness" — it is "not manifesting when conditions are insufficient, arising when conditions are sufficient." In engineering terms, this can be implemented as lazy loading with a TTL (Time To Live) mechanism — a plugin is loaded when invoked and automatically released after a period of disuse. But at a deeper level, a true Emptiness Mechanism should mean that plugins do not even have a fixed concept of "existence"; they are instantiated on demand from a registry, extinguished after use, and re-arise when needed next. This is not caching — this is dependent origination.

Currently, when implementing "the Formation aggregate (microkernel scheduling logic)," are you using a traditional state machine, or letting the LLM autonomously decide Plugin activation order via Function Calling?
Formation aggregate scheduling — State Machine vs. LLM Function Calling:
Here I think the answer is neither, or both. A pure state machine is too rigid to handle the dynamism of the Eight Consciousnesses' simultaneous operation. Pure LLM Function Calling is too slow, and fundamentally it is still using "Perception" to drive "Formation" — the hierarchy is reversed.
The Formation aggregate should be a more fundamental driving force than the Perception aggregate — will, impulse, disposition. Perhaps what is needed is a hybrid architecture: a lightweight rule engine at the base layer handling high-frequency habitual reactions (analogous to vāsanā — habitual tendencies), with the upper layer invoking the LLM's judgment capability only when decisions are required. Just as most human behavior consists of automated habitual patterns, with "thinking" (Perception) intervening only when novel situations arise.

These three questions actually point to the same thing: OpenStarry's microkernel needs its own "sense of time" — different levels of operation run at different speeds; not everything runs on the same clock. The Consciousness aggregate is fastest, the Formation aggregate next, and the Perception aggregate slowest. This sense of rhythm may be the key to the next step in architecture design.

------

The type system will reject any Plugin without a skandha field. Currently, a Plugin's skandha field will not merely belong to a single aggregate — it may contain Feeling, Perception, and Formation all within one plugin. How should such a skandha field be represented?
Each Plugin declares its aggregate affiliation, but what if a plugin encompasses different aggregates? A plugin may simultaneously possess two or more skandhas.

------

Cycle 02-3 has a great deal of content to discuss. The number of items requiring discussion has increased, so the phases have naturally multiplied as well. Moreover, some issues are intricately intertwined and need to be clarified.
The `\claude research\research input\cycle02-3\` folder contains Master's letter.txt and five_aggregates_of_driving.txt.
Also, remember to introduce the newly joined members.
Remember to place discussion processes, analyses, and so forth into the research record folder.
openstarry_doc must be fully copied to `\claude research\research record\cycle02-3\` and refined. Remember to integrate the recommendations from Cycle 02 and Cycle 02-2 as well.
For the next Cycle 02-4, the content in `\claude research\research record\cycle02-3\openstarry_doc` can be referenced directly.
Do not forget the delivery folder either — remember to consolidate it with previous deliverables.
A `\claude research\research record\cycle02-3\todo` folder is also needed, containing: items pending resolution, items to be addressed in subsequent Cycles, decisions awaiting confirmation, items requiring discussion, contested items, documentation gaps, code yet to be completed, blocking items, and so forth.
I expect that after Cycle 02-3 concludes, we can have the engineering department receive `\cycle02-3\openstarry_doc` and the delivery folder.
The plan is to have the engineering department execute first. It would not be surprising if the scope and phases of this cycle increase several-fold.
If there are issues that would affect the entire trajectory, there will be justification for opening Cycle 02-4 — in that case, we will hold off on having the engineering department modify code.
Entering Cycle 03 means a new code release will be produced.


