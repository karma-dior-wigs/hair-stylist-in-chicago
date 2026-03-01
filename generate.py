import os
from datetime import datetime

# Official Chicago ZIP Codes
zip_codes = [
"60601","60602","60603","60604","60605","60606","60607","60608","60609","60610",
"60611","60612","60613","60614","60615","60616","60617","60618","60619","60620",
"60621","60622","60623","60624","60625","60626","60628","60629","60630","60631",
"60632","60633","60634","60636","60637","60638","60639","60640","60641","60642",
"60643","60644","60645","60646","60647","60649","60651","60652","60653","60654",
"60655","60656","60657","60659","60660","60661","60707"
]

base_url = "https://karma-dior-wigs.github.io/hair-stylist-in-chicago/index.html"  # CHANGE THIS

template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Black Wig Stylist in {zip} | Karma Dior Chicago</title>
<meta name="description" content="Looking for a Black wig stylist near {zip}? Karma Dior specializes in custom wigs and lace installs serving Chicago. Appointment-only.">

<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">

<style>
body {{
  font-family: 'Inter', sans-serif;
  background: #f9e9ef;
  color: #000;
  padding: 4rem 1.5rem;
  max-width: 950px;
  margin: auto;
  line-height: 1.7;
}}

h1 {{
  font-family: 'Playfair Display', serif;
  font-size: 2.5rem;
}}

a {{
  color: #C6A75E;
  font-weight: 500;
  text-decoration: none;
}}

a:hover {{
  text-decoration: underline;
}}
</style>

<script type="application/ld+json">
{{
 "@context": "https://schema.org",
 "@type": "BeautySalon",
 "name": "Karma Dior",
 "areaServed": "Chicago {zip}",
 "description": "Black wig stylist in Chicago specializing in custom wigs and lace installs.",
 "priceRange": "$$"
}}
</script>

</head>
<body>

<h1>Luxury Black Wig Stylist Serving {zip}</h1>

<p>
If you are located in {zip} and searching for a professional wig install,
Karma Dior provides luxury custom wigs and lace installs tailored for Black women in Chicago.
</p>

<p>
Services include custom wig creation, wig + install packages,
lace customization, coloring, deep cleansing, and precision baby hair styling.
</p>

<p>
All services are appointment-only and require a $50 non-refundable deposit to secure booking.
</p>

<p>
<a href="/index.html">Return to Main Site</a>
</p>

</body>
</html>
"""

# Generate ZIP pages
for zip_code in zip_codes:
    with open(f"{zip_code}.html", "w") as f:
        f.write(template.format(zip=zip_code))

# Generate sitemap
with open("sitemap.xml", "w") as sitemap:
    sitemap.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    sitemap.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    for zip_code in zip_codes:
        sitemap.write("  <url>\n")
        sitemap.write(f"    <loc>{base_url}/{zip_code}.html</loc>\n")
        sitemap.write(f"    <lastmod>{datetime.utcnow().date()}</lastmod>\n")
        sitemap.write("  </url>\n")

    sitemap.write("</urlset>")

print("All Chicago ZIP pages + sitemap generated successfully.")
