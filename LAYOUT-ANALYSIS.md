# JAMMIX Original Site Layout Analysis

## Desktop Layout (1920x1080)

### Header
- Height: 55px
- Background: Coral (#EC7969) with pink border bottom (#F26687, 7px)
- Content: "Operator Guide & Build Videos" link, "Purchase JAMMIX" button, X icon
- NO JAMMIX logo text in header
- Full width

### Main Content Area
- Total page height: ~4869px
- Content width: 980px centered (leaves ~470px margin on each side = ~24.5% each side)
- Split into two columns within the 980px:
  - LEFT (~50%): Scrollable content (hero text, features, galleries, JAMMIX footer logo)
  - RIGHT (~50%): FIXED PCB image that stays in place while left side scrolls

### Fixed Right Panel
- PCB image (jammix-board.png) - 556x620px
- Position: fixed
- Stays visible throughout page scroll
- Gray background (#262626) matching hero section

### Sections (Left Side, Top to Bottom)
1. **Hero**: JAMMIX title (coral, stencil font ~152px), tagline, platforms list, description, "for MiSTer" badge
2. **Features**: Bullet point list (single column)
3. **Gallery 1 - Console ITX**: Title + description + images (single column on desktop within left pane)
4. **Gallery 2 - Arcade**: Title + description + images
5. **Specs/Notes**: Requirements list
6. **Footer Logo**: Large JAMMIX stencil text (coral, ~97px)

## Mobile Layout (390x844)

### Header
- Same coral bar, narrower
- "Operator Guide & Build Videos" + X icon only
- "Purchase JAMMIX" may stack or be in menu

### Content
- Single column, full width with small padding
- Hero image (PCB) OVERLAPS with hero text content
- Text wraps around/beside the PCB image
- After hero section, everything stacks vertically
- Gallery images: single column
- JAMMIX footer logo at bottom

## Key Measurements
- Header height: 55px
- Border: 7px pink
- Content max-width: 980px
- Side margins: ~10% (when full width) or auto-centered
- Background colors: #1D1D1D (dark), #262626 (hero/sections)

## Implementation Strategy
1. Simple header bar (fixed/sticky)
2. Two-column grid on desktop: left scrollable, right fixed
3. Collapse to single column on mobile with overlapping hero
4. No complex footer - just centered JAMMIX logo
