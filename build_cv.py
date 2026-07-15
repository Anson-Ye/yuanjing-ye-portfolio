from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

OUT = "assets/My-CV.pdf"
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=23, leading=26, textColor=colors.HexColor("#17332c"), spaceAfter=5))
styles.add(ParagraphStyle(name="Contact", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=13, textColor=colors.HexColor("#405048"), spaceAfter=13))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=colors.HexColor("#17332c"), spaceBefore=12, spaceAfter=5))
styles.add(ParagraphStyle(name="Body2", parent=styles["Normal"], fontName="Helvetica", fontSize=9.4, leading=13, spaceAfter=4))
styles.add(ParagraphStyle(name="Role", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=colors.HexColor("#17332c"), spaceBefore=5, spaceAfter=2))

def bullet(text):
    return Paragraph("• " + text, styles["Body2"])

story = [
    Paragraph("YuanJing Ye", styles["Name"]),
    Paragraph("410114332@icl.school.nz &nbsp; | &nbsp; +64 22 386 9988", styles["Contact"]),
    Paragraph("PROFESSIONAL PROFILE", styles["Section"]),
    Paragraph("Commercial leader with senior experience in sales, marketing, e-commerce and business operations. Experienced in leading cross-functional teams, developing international customer relationships and supporting growth through trade shows, digital channels and marketplace platforms. Fluent in English and Chinese.", styles["Body2"]),
    Paragraph("CORE SKILLS", styles["Section"]),
    bullet("Inspirational team leadership and high-performance culture development."),
    bullet("B2B, B2C, direct-to-consumer and e-commerce strategy."),
    bullet("Sales and marketing, customer relationships, trade-show representation and social-media campaigns."),
    bullet("Microsoft Office, Google Workspace, HubSpot, Amazon, Shopify and WordPress."),
    bullet("Adobe Creative Suite and media production including photo editing, video production and graphic design."),
    Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"]),
    Paragraph("Sales and Marketing Director | Shenzhen Kabei Electronics Co., Ltd | Sep 2022 – May 2025", styles["Role"]),
    bullet("Led a ten-person sales and marketing team, contributing to annual sales turnover of approximately USD 15 million."),
    bullet("Represented the company at global trade shows including CES and HKTDC Fair; developed customer relationships and market insight."),
    bullet("Promoted the business across Amazon, Alibaba and social-media channels; coordinated content and multi-platform advertising activity."),
    bullet("Prepared monthly reports, handled VIP deals and delivered staff training in a fast-paced commercial environment."),
    Paragraph("Chief Executive Officer | Shenzhen iPeace Entity Co. Ltd | Mar 2014 – Aug 2022", styles["Role"]),
    bullet("Set strategic direction, operational plans and management processes aligned with the organisation’s vision and mission."),
    bullet("Led market analysis, product research, brand promotion and cross-functional collaboration across product, engineering, sales and marketing."),
    bullet("Developed B2B, B2C and direct-to-consumer business channels, with responsibility for revenue growth, profitability and sustainability."),
    bullet("Led continuous improvement in supply chain management, quality control, customer satisfaction and organisational development."),
    Paragraph("EDUCATION", styles["Section"]),
    Paragraph("Master of Business Management | ICL Graduate Business School, New Zealand", styles["Body2"]),
    Paragraph("Undergraduate study in English | Guangdong University of Foreign Studies, China", styles["Body2"]),
    Paragraph("CERTIFICATIONS & INTELLECTUAL PROPERTY", styles["Section"]),
    Paragraph("Certificate of Computer Information Technology Testing | Ministry of Human Resources of the People’s Republic of China | Certificate No. 201300230653906", styles["Body2"]),
    Paragraph("Patent of Invention: A watch containing an integrated ceramic case | China National Intellectual Property Administration | Patent No. ZL201320528360.X", styles["Body2"]),
]
doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=22*mm, rightMargin=22*mm, topMargin=19*mm, bottomMargin=18*mm, title="YuanJing Ye CV")
doc.build(story)
