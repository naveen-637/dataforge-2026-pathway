from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path

OUT=Path('/mnt/data/dataforge_pathway_recurrent_memory')

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleDF', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=21, leading=23, spaceAfter=10, textColor=colors.HexColor('#111318')))
styles.add(ParagraphStyle(name='H1DF', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=15, leading=18, spaceBefore=8, spaceAfter=6, textColor=colors.HexColor('#111318')))
styles.add(ParagraphStyle(name='BodyDF', parent=styles['BodyText'], fontName='Helvetica', fontSize=8.4, leading=10.7, spaceAfter=3, textColor=colors.HexColor('#22262b')))
styles.add(ParagraphStyle(name='SmallDF', parent=styles['BodyText'], fontName='Helvetica', fontSize=7.2, leading=9.2, textColor=colors.HexColor('#4d555d')))
styles.add(ParagraphStyle(name='FormulaDF', parent=styles['BodyText'], fontName='Courier', fontSize=9.5, leading=12, backColor=colors.HexColor('#f1f3f5'), borderPadding=6, textColor=colors.HexColor('#111318'), spaceAfter=7))
styles.add(ParagraphStyle(name='BoxDF', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=10, leading=13, backColor=colors.HexColor('#eef5f9'), borderColor=colors.HexColor('#8aa8bc'), borderWidth=0.6, borderPadding=8, spaceAfter=8, textColor=colors.HexColor('#163040')))


def header_footer(canvas, doc):
    canvas.saveState()
    w,h=A4
    canvas.setFont('Helvetica',7)
    canvas.setFillColor(colors.HexColor('#66707a'))
    canvas.drawString(18*mm, 10*mm, 'DataForge 2026 · Recurrent Memory Lab')
    canvas.drawRightString(w-18*mm, 10*mm, f'{doc.page}')
    canvas.restoreState()

summary_text = [
"In-context learning asks a simple architectural question: what carries demonstrations forward as computation proceeds? A recurrent-memory model compresses the stream into an evolving state that is repeatedly read and updated. Unlike a token-by-token history, the state shape can remain fixed as the sequence grows, but compression can create interference and forgetting.",
"<b>Falsifiable claim:</b> adding demonstrations can be absorbed into a fixed-size recurrent state, but overlapping evidence can interfere and cause retrieval errors. The artifact uses a deliberately small 5 x 5 associative-memory substrate. A demonstration provides a key vector k and value vector v; the toy writes an outer product into a fixed matrix with decay: <font name='Courier'>M_t = lambda M_(t-1) + alpha k_t v_t^T</font>. A query reads <font name='Courier'>q^T M_t</font> and returns scores over candidate values. The learner can add examples without increasing the matrix dimensions, then increase key similarity or add a conflicting example to make crosstalk visible beside ground truth.",
"The computation is a <b>synthetic teaching toy</b>, not an official BDH or BDH-CQ implementation. Its role is to expose state, write, read, capacity and interference as visible variables. The narrow experiment is deliberately stronger than a static definition because a learner can change one variable and test whether the predicted consequence appears.",
"The BDH connection is substantive but carefully bounded. The Dragon Hatchling paper describes a scale-free graph of locally interacting neuron particles and states that BDH working memory during inference relies on synaptic plasticity with Hebbian learning. It also reports sparse, positive activations and emphasizes interpretability of state. This motivates the idea of memory as evolving internal state, while the official architecture is much richer than the 5 x 5 toy.",
"BDH-CQ makes the selected in-context-learning topic especially direct. Its August 2026 technical report describes inference-time inputs continuously updating recurrent memory; the query is then solved through iterative computation in a high-dimensional latent space without verbalizing intermediate reasoning. The correct teaching bridge is therefore: <b>demonstrations update state -> state supports the query -> latent computation can refine the answer.</b> The toy teaches the first two pieces and uses the paper for the third, without claiming behavioral equivalence.",
"The idea is active across current sequence-model research. Griffin (2024) combines gated linear recurrences with local attention; RecurrentGemma (2024) applies the Griffin design in open language models and highlights fixed-sized state; Titans (2025) introduces learned neural long-term memory for historical context. These works, together with BDH and BDH-CQ, show recurrent state and learned memory as active post-Transformer design directions, not merely historical RNN ideas.",
"The main limitation is unavoidable: fixed state is not infinite memory. Similar inputs can compete for the same representational directions, while decay can both preserve capacity and erase useful evidence. The toy does not establish benchmark-level reasoning, and recurrent memory is not automatically 'reasoning'. A useful learner outcome is more precise: explain what stayed fixed, what changed, why the estimate moved, and how that mechanism resembles - but is not identical to - recurrent memory in BDH-CQ."
]


sources = [
"[1] Kosowski, A. et al. (2025). The Dragon Hatchling: The Missing Link between the Transformer and Models of the Brain. arXiv:2509.26507. https://arxiv.org/abs/2509.26507",
"[2] Engdahl, B. et al. (2026). BDH-CQ: In-Context Learning with Recurrent Latent Reasoning. arXiv:2608.09888. https://arxiv.org/abs/2608.09888",
"[3] De, S. et al. (2024). Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models. arXiv:2402.19427. https://arxiv.org/abs/2402.19427",
"[4] Botev, A. et al. (2024). RecurrentGemma: Moving Past Transformers for Efficient Open Language Models. arXiv:2404.07839. https://arxiv.org/abs/2404.07839",
"[5] Behrouz, A., Zhong, P., Mirrokni, V. (2025). Titans: Learning to Memorize at Test Time. arXiv:2501.00663. https://arxiv.org/abs/2501.00663",
"[6] Pathway (2026). The Equations of Reasoning. https://pathway.com/research/the-equations-of-reasoning",
]

# one-page summary
summary_path=OUT/'one_page_concept_summary.pdf'
doc=SimpleDocTemplate(str(summary_path), pagesize=A4, rightMargin=15*mm, leftMargin=15*mm, topMargin=13*mm, bottomMargin=15*mm)
story=[Paragraph('Recurrent Memory: Learning from Demonstrations Without Growing the State', styles['TitleDF']),
       Paragraph('DataForge 2026 · Pathway Track · One-page concept summary', styles['SmallDF']), Spacer(1,5)]
story.append(Paragraph('<b>Central claim.</b> Adding demonstrations can be absorbed into a fixed-size recurrent state, but overlapping evidence can interfere and cause retrieval errors.', styles['BoxDF']))
for p in summary_text: story.append(Paragraph(p, styles['BodyDF']))
story.append(Paragraph('Representative research comparison', styles['H1DF']))
data=[['System / work','Core memory idea','Why it matters here'],
      ['Griffin / RecurrentGemma (2024)','Gated recurrent state + local attention','Concrete modern recurrent sequence modeling with fixed-size state.'],
      ['Titans (2025)','Learned neural long-term memory','Shows active work on storing long past context in learned memory.'],
      ['BDH / BDH-CQ (2025-2026)','Synaptic or recurrent latent memory','Direct Pathway link: evolving inference-time state stores and supports new information.']]
t=Table(data,colWidths=[38*mm,57*mm,78*mm], repeatRows=1)
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#edf0f3')),('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#cbd1d7')),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),6.7),('LEADING',(0,0),(-1,-1),8.2),('VALIGN',(0,0),(-1,-1),'TOP'),('TEXTCOLOR',(0,0),(-1,-1),colors.HexColor('#24292f')),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
story.append(t)
story.append(Spacer(1,6))
story.append(Paragraph('Evidence discipline: the interactive substrate is synthetic and educational. It demonstrates the mechanics of a recurrent associative state, not an official BDH/BDH-CQ checkpoint. Claims about BDH and BDH-CQ are sourced to the primary papers above.', styles['SmallDF']))
story.append(Spacer(1,3))
for s in sources: story.append(Paragraph(s, styles['SmallDF']))
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)

# Blog PDF
blog_path=OUT/'blog.pdf'
doc=SimpleDocTemplate(str(blog_path), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=15*mm, bottomMargin=16*mm)
story=[Paragraph('Recurrent Memory Lab', styles['TitleDF']), Paragraph('How a fixed-size state can learn from demonstrations - and how it can forget', styles['SmallDF']), Spacer(1,6)]
sections=[
('1. The idea in one sentence', '<b>A recurrent state can absorb a growing stream of demonstrations without growing its shape, but compression makes interference and forgetting possible.</b>'),
('2. Start with a learner-visible substrate', 'The demo is deliberately tiny. A 5 x 5 matrix is the memory. Each demonstration writes a key/value association by an outer product; each query projects a key through the accumulated matrix. The point is not to make a powerful model. The point is to expose the variable that normally disappears inside a large neural network: <i>state</i>.'),
('3. The live experiment', 'The page opens with a clean preset, so the learner immediately sees a correct prediction. Adding demonstrations changes the state but not its dimensions. A similarity slider makes distinct keys share representational features. A conflict button adds a wrong association for the query key. The output shows ground truth, prediction, and the score vector side by side. This turns the claim into something the learner can challenge.'),
('4. Why fixed size matters', 'A token-by-token cache stores a growing record of past representations. A recurrent memory instead carries forward a summary. This can reduce the amount of inference-time memory that must grow with sequence length, but the summary is necessarily lossy in some tasks. The educational interface makes the trade-off concrete: five columns remain five columns while more evidence is written.'),
('5. Why interference matters', 'Suppose two keys are orthogonal. A write to one key does not affect the other in the idealized toy. Now make their vectors similar. The outer-product writes share representational directions, so reading one key can recover value components contributed by another. This is the same kind of capacity/crosstalk question that appears whenever many experiences are compressed into one evolving state.'),
('6. BDH: from matrix toy to synaptic dynamics', 'Dragon Hatchling (BDH) is a substantially richer research architecture. Its paper describes a scale-free graph of locally interacting neuron particles and reports that working memory during inference relies on synaptic plasticity with Hebbian learning. The paper also studies sparse positive activations and interpretable state. The correct pedagogical bridge is therefore: the toy makes “memory as evolving internal state” visible; BDH provides a concrete frontier architecture in which memory is implemented through learned local dynamics. The toy is not BDH and should never be presented as a faithful reimplementation.'),
('7. BDH-CQ: the in-context-learning bridge', 'BDH-CQ is especially aligned with the chosen topic. Its 2026 technical report describes inference-time inputs continuously updating recurrent memory, after which a query is solved through iterative computation in a high-dimensional latent space without verbalizing intermediate reasoning. This gives the learner a clean conceptual picture: demonstrations update internal state; state supports the query; additional latent computation can refine the solution. The artifact teaches the first two pieces directly and uses the paper to explain the third, without pretending the browser toy reproduces the 150M-parameter model.'),
('8. Frontier context', 'The concept is active well beyond BDH. Griffin combines gated linear recurrences with local attention. RecurrentGemma packages the Griffin architecture into open language models and emphasizes the efficiency of a fixed-sized recurrent state. Titans introduces a learned neural long-term memory for historical context and reports experiments on very long contexts. These systems make the same design pressure visible from different directions: keep useful information available without paying the full cost of carrying every prior token through every future operation.'),
('9. What the demo does not prove', 'The demo does not prove that recurrent memory is better than Transformer attention, that fixed-size state is sufficient for arbitrary tasks, or that BDH-CQ performance follows from the toy equation. It does prove something narrower: under the toy dynamics, the state shape stays fixed while demonstrations accumulate, and controlled similarity/conflict can change retrieval accuracy. That narrow claim is exactly why the experiment is useful.'),
('10. 60-second lesson', 'Load the preset. Query B. Confirm the truth. Increase key similarity. Add a conflicting demonstration. Query B again. Then explain: (a) what stayed fixed, (b) what changed, (c) why the estimate shifted, and (d) how that resembles but does not equal recurrent memory in BDH-CQ. A successful lesson is not “recurrent models are good”; it is a mechanistic explanation of a measurable trade-off.')]
for h,b in sections:
    story.append(Paragraph(h, styles['H1DF']))
    story.append(Paragraph(b, styles['BodyDF']))
    if h.startswith('2.') or h.startswith('6.') or h.startswith('7.'):
        story.append(Spacer(1,2))
        story.append(Paragraph('Teaching equation / evidence boundary: <font name="Courier">M_t = lambda M_(t-1) + alpha k_t v_t^T</font> (toy only). Official BDH uses richer neuron/synapse dynamics; BDH-CQ is the published recurrent-latent model described in source [2].', styles['FormulaDF']))
story.append(PageBreak())
story.append(Paragraph('Research notes and source map', styles['H1DF']))
source_table=[['Claim used in this blog','Primary source'],
 ['BDH uses synaptic plasticity / Hebbian working memory and a brain-inspired graph','[1] BDH paper'],
 ['BDH-CQ updates recurrent memory at inference and performs latent iterative reasoning','[2] BDH-CQ paper'],
 ['Gated linear recurrences and local attention can support efficient language models','[3] Griffin'],
 ['RecurrentGemma is an open model family built on Griffin and uses fixed-sized state','[4] RecurrentGemma'],
 ['Neural long-term memory can learn to memorize historical context at test time','[5] Titans'],
 ['Pathway frames local neuron/synapse dynamics as the basis for memory and reasoning','[6] Equations of Reasoning']]
t2=Table(source_table,colWidths=[91*mm,76*mm], repeatRows=1)
t2.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#edf0f3')),('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#cbd1d7')),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),7),('LEADING',(0,0),(-1,-1),9),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
story.append(t2)
story.append(Spacer(1,9))
story.append(Paragraph('Full references', styles['H1DF']))
for s in sources: story.append(Paragraph(s, styles['BodyDF']))
story.append(Spacer(1,9))
story.append(Paragraph('Implementation and provenance', styles['H1DF']))
story.append(Paragraph('The browser artifact is original JavaScript/HTML/CSS with no third-party libraries. The synthetic key/value examples are original. AI assistance was used for research organization, drafting, and initial code generation; the repository explicitly discloses this and requires human review of every claim and implementation detail. The code is MIT licensed.', styles['BodyDF']))
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(summary_path)
print(blog_path)
