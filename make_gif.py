from datetime import datetime, timezone
import gifos

DEVOS_INIT_DATE = datetime(2023, 8, 14, 0, 0, 0, tzinfo=timezone.utc)
TRIMIUM_INIT_DATE = datetime(2025, 12, 1, 0, 0, 0, tzinfo=timezone.utc)
TALKASAURUS_INIT_DATE = datetime(2026, 1, 15, 0, 0, 0, tzinfo=timezone.utc)

RESET = "\x1b[0m"
GRAY, RED, GREEN, YELLOW, CYAN, WHITE = (f"\x1b[{c}m" for c in (90, 91, 92, 93, 96, 97))
SPINNER = ["*     ", "**    ", "***   ", " ***  ", "  *** ", "   ** ", "    * ", "   ** ", "  *** ", " ***  ", "***   ", "**    "]
LABEL_WIDTH = 34
BAR_WIDTH = 32


def get_uptime_prompt() -> str:
    now = datetime.now(timezone.utc)
    diff = now - DEVOS_INIT_DATE
    days = max(0, diff.days)
    hours = diff.seconds // 3600
    return f"up {days}d {hours:02d}h"


def get_system_uptime_detailed() -> str:
    now = datetime.now(timezone.utc)
    diff = now - DEVOS_INIT_DATE
    days = max(0, diff.days)
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    return f"{days} days, {hours} hours, {minutes} mins"


def get_container_uptime_short(init_date: datetime) -> str:
    now = datetime.now(timezone.utc)
    diff = now - init_date
    days = max(0, diff.days)
    if days >= 60:
        months = days // 30
        return f"Up {months} months"
    elif days >= 30:
        return "Up 1 month"
    elif days >= 7:
        weeks = days // 7
        return f"Up {weeks} weeks"
    elif days > 0:
        return f"Up {days} days"
    else:
        hours = max(1, diff.seconds // 3600)
        return f"Up {hours} hours"


def get_container_uptime_detailed(init_date: datetime) -> str:
    now = datetime.now(timezone.utc)
    diff = now - init_date
    days = max(0, diff.days)
    months = days // 30
    if months > 0:
        return f"Up {months} months ({days} days)"
    return f"Up {days} days"


def get_prompt() -> str:
    return f"{GREEN}devtrivedi@DevOS{RESET} {GRAY}[{CYAN}{get_uptime_prompt()}{GRAY}]{RESET}:{CYAN}~{RESET}$ "


def scene_boot(t):
    t.gen_text(f"{WHITE}GNU GRUB  version 2.06{RESET}", 5, count=5)
    t.gen_text("Loading DevOS", 6, count=1)
    t.toggle_show_cursor(True)
    t.gen_typing_text("...", 6, contin=True, speed=2)
    t.toggle_show_cursor(False)
    t.gen_text("", 6, count=3, contin=True)

    t.toggle_show_cursor(False)
    for f in range(6):
        t.delete_row(8)
        t.gen_text(
            f"{GRAY}[{YELLOW}{SPINNER[f % len(SPINNER)]}{GRAY}]{RESET} Reached target Origin",
            8,
            count=1,
            contin=True,
        )

    t.delete_row(8)
    t.gen_text(
        f"{GRAY}[{GREEN}  OK  {GRAY}]{RESET} Reached target Origin "
        f"{GRAY}{'.' * (LABEL_WIDTH - len('Reached target Origin') - 1)}{RESET} ",
        8,
        count=1,
        contin=True,
    )
    t.gen_text(f"{CYAN}Jamnagar, Gujarat{RESET}", 8, contin=True, count=7)

    t.toggle_show_cursor(False)
    for f in range(16):
        t.delete_row(9)
        t.gen_text(
            f"{GRAY}[{YELLOW}{SPINNER[f % len(SPINNER)]}{GRAY}]{RESET} Passed JEE Main",
            9,
            count=1,
            contin=True,
        )

        pct = 99.02 * (1 - (1 - (f + 1) / 16) ** 3)
        filled = int(BAR_WIDTH * pct / 100)
        head = ">" if filled < BAR_WIDTH else "="
        bar = "=" * max(filled - 1, 0) + head if filled else ""

        t.delete_row(10)
        t.gen_text(
            f"{' ' * 9}{GRAY}[{CYAN}{bar:<{BAR_WIDTH}}{GRAY}]{RESET} "
            f"{WHITE}{pct:5.2f}%{RESET}",
            10,
            count=1,
            contin=True,
        )

    t.delete_row(9)
    t.gen_text(
        f"{GRAY}[{GREEN}  OK  {GRAY}]{RESET} Passed JEE Main "
        f"{GRAY}{'.' * (LABEL_WIDTH - len('Passed JEE Main') - 1)}{RESET} ",
        9,
        count=1,
        contin=True,
    )
    t.gen_text(f"{YELLOW}99.02 percentile{RESET}", 9, contin=True, count=8)

    t.toggle_show_cursor(False)
    for f in range(6):
        t.delete_row(11)
        t.gen_text(
            f"{GRAY}[{YELLOW}{SPINNER[f % len(SPINNER)]}{GRAY}]{RESET} Mounted /dev/dau",
            11,
            count=1,
            contin=True,
        )

    t.delete_row(11)
    t.gen_text(
        f"{GRAY}[{GREEN}  OK  {GRAY}]{RESET} Mounted /dev/dau "
        f"{GRAY}{'.' * (LABEL_WIDTH - len('Mounted /dev/dau') - 1)}{RESET} ",
        11,
        count=1,
        contin=True,
    )
    t.gen_text(f"{CYAN}Dhirubhai Ambani University, 2023{RESET}", 11, contin=True, count=7)

    t.toggle_show_cursor(False)
    for f in range(8):
        t.delete_row(12)
        t.gen_text(
            f"{GRAY}[{YELLOW}{SPINNER[f % len(SPINNER)]}{GRAY}]{RESET} Started goldman.service",
            12,
            count=1,
            contin=True,
        )

    t.delete_row(12)
    t.gen_text(
        f"{GRAY}[{GREEN}  OK  {GRAY}]{RESET} Started goldman.service "
        f"{GRAY}{'.' * (LABEL_WIDTH - len('Started goldman.service') - 1)}{RESET} ",
        12,
        count=1,
        contin=True,
    )
    t.gen_text(f"{YELLOW}Summer Analyst, Bengaluru, 2026{RESET}", 12, contin=True, count=8)

    t.toggle_show_cursor(False)
    for f in range(6):
        t.delete_row(13)
        t.gen_text(
            f"{GRAY}[{YELLOW}{SPINNER[f % len(SPINNER)]}{GRAY}]{RESET} Started teaching.service (bg)",
            13,
            count=1,
            contin=True,
        )

    t.delete_row(13)
    t.gen_text(
        f"{GRAY}[{GREEN}  OK  {GRAY}]{RESET} Started teaching.service (bg) "
        f"{GRAY}{'.' * (LABEL_WIDTH - len('Started teaching.service (bg)') - 1)}{RESET} ",
        13,
        count=1,
        contin=True,
    )
    t.gen_text(f"{CYAN}Part-time Teaching Assistant, DAU{RESET}", 13, contin=True, count=7)

    t.toggle_show_cursor(False)
    for f in range(6):
        t.delete_row(14)
        t.gen_text(
            f"{GRAY}[{YELLOW}{SPINNER[f % len(SPINNER)]}{GRAY}]{RESET} Reached target Backend Engineer",
            14,
            count=1,
            contin=True,
        )

    t.delete_row(14)
    t.gen_text(
        f"{GRAY}[{GREEN}  OK  {GRAY}]{RESET} {GREEN}Reached target Backend Engineer{RESET}",
        14,
        count=8,
        contin=True,
    )

    t.gen_text(f"{YELLOW}DevOS 1.0 (tty1){RESET}", 16, count=5)
    t.gen_text("login: ", 18, count=4)
    t.toggle_show_cursor(True)
    t.gen_typing_text("devtrivedi", 18, contin=True, speed=2)
    t.gen_text("", 18, count=5, contin=True)

    t.toggle_show_cursor(False)
    t.gen_text("Password: ", 19, count=3)
    t.toggle_show_cursor(True)
    for _ in range(10):
        t.gen_text("*", 19, count=2, contin=True)
    t.gen_text("", 19, count=5, contin=True)
    t.toggle_show_cursor(False)

    for r in range(1, 25):
        t.delete_row(r)
    t.gen_text("", 1, count=5)


def scene_whoami(t):
    t.toggle_show_cursor(False)

    t.gen_text(get_prompt(), 2, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text(f"{WHITE}whoami{RESET}", 2, contin=True, speed=2)
    t.toggle_show_cursor(False)
    t.gen_text("", 2, count=5, contin=True)

    FIELDS = [
        ("Name",      "Dev Trivedi",                    WHITE),
        ("Age",       "21",                             WHITE),
        ("Origin",    "Jamnagar, Gujarat",              WHITE),
        ("Base",      "Gandhinagar, Gujarat",           WHITE),
        ("Formarly",  "Summer Analyst @ Goldman Sachs", YELLOW),
        ("Role",      "Backend Engineer",               YELLOW),
        ("Focus",     "Distributed Systems, LLM Infra", WHITE),
        ("Education", "B.Tech ICT @ DAU, 2023-Present", WHITE),
        ("CGPA",      "8.59",                           WHITE),
        ("Status",    "Open to backend roles",          WHITE),
    ]

    for i, (k, v, col) in enumerate(FIELDS):
        dots = "." * (25 - len(k))
        t.gen_text(
            f"{CYAN}{k}{RESET} {GRAY}{dots}{RESET} {col}{v}{RESET}",
            4 + i,
            count=2,
            contin=True,
        )

    t.gen_text("", 15, count=6, contin=True)

    t.gen_text(
        get_prompt(),
        16,
        count=15,
        contin=True,
    )
    t.toggle_show_cursor(True)
    t.gen_text("", 16, count=39, contin=True)


def scene_skills(t):
    t.toggle_show_cursor(False)

    t.gen_text(get_prompt(), 2, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text(f"{WHITE}cat SKILLS.md{RESET}", 2, contin=True, speed=1)
    t.toggle_show_cursor(False)
    t.gen_text("", 2, count=5, contin=True)

    t.gen_text(f"{CYAN}# Skills{RESET}", 4, count=2, contin=True)
    t.gen_text("", 5, count=2, contin=True)

    t.gen_text(f"{CYAN}## Languages{RESET}", 6, count=2, contin=True)
    t.gen_text(
        f"{WHITE}TypeScript {GRAY}|{RESET} "
        f"{WHITE}JavaScript {GRAY}|{RESET} "
        f"{WHITE}C {GRAY}|{RESET} "
        f"{WHITE}C++ {GRAY}|{RESET} "
        f"{WHITE}SQL{RESET}",
        7,
        count=2,
        contin=True,
    )
    t.gen_text("", 8, count=2, contin=True)

    t.gen_text(f"{CYAN}## Frameworks & Libraries{RESET}", 9, count=2, contin=True)
    t.gen_text(
        f"{WHITE}Node.js {GRAY}|{RESET} "
        f"{WHITE}Express.js {GRAY}|{RESET} "
        f"{WHITE}BullMQ {GRAY}|{RESET} "
        f"{WHITE}Next.js {GRAY}|{RESET} "
        f"{WHITE}React.js {GRAY}|{RESET} "
        f"{WHITE}Tailwind{RESET}",
        10,
        count=2,
        contin=True,
    )
    t.gen_text("", 11, count=2, contin=True)

    t.gen_text(f"{CYAN}## Databases & ORM{RESET}", 12, count=2, contin=True)
    t.gen_text(
        f"{WHITE}PostgreSQL {GRAY}|{RESET} "
        f"{WHITE}MongoDB {GRAY}|{RESET} "
        f"{WHITE}Redis {GRAY}|{RESET} "
        f"{WHITE}Prisma {GRAY}|{RESET} "
        f"{WHITE}Mongoose{RESET}",
        13,
        count=2,
        contin=True,
    )
    t.gen_text("", 14, count=2, contin=True)

    t.gen_text(f"{CYAN}## Cloud & DevOps{RESET}", 15, count=2, contin=True)
    t.gen_text(
        f"{WHITE}AWS (EC2, S3) {GRAY}|{RESET} "
        f"{WHITE}Docker {GRAY}|{RESET} "
        f"{WHITE}Nginx {GRAY}|{RESET} "
        f"{WHITE}PM2 {GRAY}|{RESET} "
        f"{WHITE}Git {GRAY}|{RESET} "
        f"{WHITE}Linux{RESET}",
        16,
        count=2,
        contin=True,
    )
    t.gen_text(
        f"{WHITE}CI/CD {GRAY}|{RESET} "
        f"{WHITE}Vercel {GRAY}|{RESET} "
        f"{WHITE}Render {GRAY}|{RESET} "
        f"{WHITE}Ollama{RESET}",
        17,
        count=2,
        contin=True,
    )

    t.gen_text("", 18, count=6, contin=True)

    t.gen_text(
        get_prompt(),
        19,
        count=15,
        contin=True,
    )
    t.toggle_show_cursor(True)
    t.gen_text("", 19, count=39, contin=True)


def scene_contact(t):
    t.toggle_show_cursor(False)

    t.gen_text(get_prompt(), 2, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text(f"{WHITE}cat contact.txt{RESET}", 2, contin=True, speed=1)
    t.toggle_show_cursor(False)
    t.gen_text("", 2, count=5, contin=True)

    FIELDS = [
        ("email",    "devtrivedi.work@gmail.com",          WHITE),
        ("phone",    "+91 8000051660",                     WHITE),
        ("linkedin", "linkedin.com/in/contact-devtrivedi", WHITE),
        ("github",   "github.com/IamDevTrivedi",           YELLOW),
        ("web",      "https://trivedi.dev",                WHITE),
    ]

    for i, (k, v, col) in enumerate(FIELDS):
        t.gen_text(
            f"{CYAN}{k:<9}{RESET} {col}{v}{RESET}",
            4 + i,
            count=2,
            contin=True,
        )

    t.gen_text("", 10, count=6, contin=True)

    t.gen_text(
        get_prompt(),
        11,
        count=15,
        contin=True,
    )
    t.toggle_show_cursor(True)
    t.gen_text("", 11, count=39, contin=True)


def scene_docker_ps(t):
    t.toggle_show_cursor(False)

    t.gen_text(get_prompt(), 2, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text(f"{WHITE}docker ps -a{RESET}", 2, contin=True, speed=1)
    t.toggle_show_cursor(False)
    t.gen_text("", 2, count=5, contin=True)

    trimium_status = get_container_uptime_short(TRIMIUM_INIT_DATE)
    talkasaurus_status = get_container_uptime_short(TALKASAURUS_INIT_DATE)

    t.gen_text(f"{CYAN}CONTAINER ID   NAME          STATUS             PORTS{RESET}", 4, count=3, contin=True)
    t.gen_text(f"{WHITE}7a3f9c2e1b04   {YELLOW}trimium{RESET}       {GREEN}{trimium_status:<18}{RESET} {WHITE}3000/tcp{RESET}",
               5, count=3, contin=True)
    t.gen_text(f"{WHITE}c4d8e1a90f27   {YELLOW}talkasaurus{RESET}   {GREEN}{talkasaurus_status:<18}{RESET} {WHITE}8080/tcp{RESET}",
               6, count=3, contin=True)

    t.gen_text("", 8, count=6, contin=True)
    t.gen_text(get_prompt(), 9, count=15, contin=True)
    t.toggle_show_cursor(True)
    t.gen_text("", 9, count=39, contin=True)


def scene_inspect_trimium(t):
    t.toggle_show_cursor(False)

    t.gen_text(get_prompt(), 2, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text(f"{WHITE}docker inspect trimium{RESET}", 2, contin=True, speed=1)
    t.toggle_show_cursor(False)
    t.gen_text("", 2, count=5, contin=True)

    status_str = get_container_uptime_detailed(TRIMIUM_INIT_DATE)
    t.gen_text(f"{CYAN}Name{RESET}    {YELLOW}trimium{RESET}  {GRAY}// Link Management & Analytics{RESET}",
               4, count=2, contin=True)
    t.gen_text(f"{CYAN}Stack{RESET}   {WHITE}Next.js | Express | MongoDB | Redis | TypeScript | AWS{RESET}",
               5, count=2, contin=True)
    t.gen_text(f"{CYAN}Status{RESET}  {GREEN}{status_str}{RESET}", 6, count=2, contin=True)
    t.gen_text("", 7, count=2, contin=True)

    t.gen_text(f"{CYAN}Highlights:{RESET}", 8, count=2, contin=True)
    t.gen_text(f"  {GRAY}-{RESET} {WHITE}Multi-tenant RBAC (Admin/Member/Viewer) | 500 URLs/batch{RESET}",
               9, count=2, contin=True)
    t.gen_text(f"  {GRAY}-{RESET} {WHITE}API latency -70% via Mongo compound indexes + cache-aside{RESET}",
               10, count=2, contin=True)
    t.gen_text(f"  {GRAY}-{RESET} {WHITE}Stateless PoW rate-limiter | zero false positives on shared IPs{RESET}",
               11, count=2, contin=True)
    t.gen_text(f"  {GRAY}-{RESET} {WHITE}GitHub Actions CI/CD | path-based monorepo | PM2 zero-downtime{RESET}",
               12, count=2, contin=True)

    t.gen_text("", 14, count=6, contin=True)
    t.gen_text(get_prompt(), 15, count=15, contin=True)
    t.toggle_show_cursor(True)
    t.gen_text("", 15, count=39, contin=True)


def scene_inspect_talkasaurus(t):
    t.toggle_show_cursor(False)

    t.gen_text(get_prompt(), 2, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text(f"{WHITE}docker inspect talkasaurus{RESET}", 2, contin=True, speed=1)
    t.toggle_show_cursor(False)
    t.gen_text("", 2, count=5, contin=True)

    status_str = get_container_uptime_detailed(TALKASAURUS_INIT_DATE)
    t.gen_text(f"{CYAN}Name{RESET}    {YELLOW}talkasaurus{RESET}  {GRAY}// AI Powered Telegram Bot{RESET}",
               4, count=2, contin=True)
    t.gen_text(f"{CYAN}Stack{RESET}   {WHITE}Telegram | PostgreSQL | Ollama | Redis | Docker{RESET}",
               5, count=2, contin=True)
    t.gen_text(f"{CYAN}Status{RESET}  {GREEN}{status_str}{RESET}", 6, count=2, contin=True)
    t.gen_text("", 7, count=2, contin=True)

    t.gen_text(f"{CYAN}Highlights:{RESET}", 8, count=2, contin=True)
    t.gen_text(f"  {GRAY}-{RESET} {WHITE}Local LLM via Ollama | dynamic prompts | multi-turn memory{RESET}",
               9, count=2, contin=True)
    t.gen_text(f"  {GRAY}-{RESET} {WHITE}5-container Docker architecture | isolated networks{RESET}",
               10, count=2, contin=True)
    t.gen_text(f"  {GRAY}-{RESET} {WHITE}Dual-mode sessions: ephemeral in-memory + AES-256 persistent{RESET}",
               11, count=2, contin=True)
    t.gen_text(f"  {GRAY}-{RESET} {WHITE}Admin dashboard: health, usage analytics, bulk broadcast{RESET}",
               12, count=2, contin=True)

    t.gen_text("", 14, count=6, contin=True)
    t.gen_text(get_prompt(), 15, count=15, contin=True)
    t.toggle_show_cursor(True)
    t.gen_text("", 15, count=39, contin=True)


def scene_experience(t):
    t.toggle_show_cursor(False)

    t.gen_text(get_prompt(), 2, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text(f"{WHITE}cat experience.log{RESET}", 2, contin=True, speed=1)
    t.toggle_show_cursor(False)
    t.gen_text("", 2, count=5, contin=True)

    LOG = [
        ("2026-05", "joined Goldman Sachs - Summer Analyst Intern, Bengaluru", YELLOW),
        ("2026-05", "Event-Triggered Automation - Python pipeline replacing manual workflow", WHITE),
        ("2026-05", "Data Pipeline - deterministic prep, grouping, materiality thresholds", WHITE),
        ("2026-06", "LLM Gateway - structural validation and bounded retry loop", WHITE),
        ("2026-06", "Evaluation Harness - LLM-as-judge across 3 metrics", WHITE),
        ("2026-06", "Real-Time Updates - SSE push for generation status", WHITE),
        ("2026-07", "signed off.", YELLOW),
    ]

    for i, (date, msg, col) in enumerate(LOG):
        t.gen_text(
            f"{GRAY}[{date}]{RESET} {col}{msg}{RESET}",
            4 + i,
            count=2,
            contin=True,
        )

    t.gen_text("", 12, count=10, contin=True)

    t.gen_text(
        get_prompt(),
        13,
        count=15,
        contin=True,
    )
    t.toggle_show_cursor(True)
    t.gen_text("", 13, count=39, contin=True)


def scene_achievements(t):
    t.toggle_show_cursor(False)

    t.gen_text(get_prompt(), 2, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text(f"{WHITE}cat achievements.md{RESET}", 2, contin=True, speed=1)
    t.toggle_show_cursor(False)
    t.gen_text("", 2, count=5, contin=True)

    t.gen_text(f"{CYAN}# Achievements{RESET}", 4, count=3, contin=True)
    t.gen_text("", 5, count=2, contin=True)

    ITEMS = [
        ("Won 1st Prize, Winter of Code 7.0 (MSTC DAU) - 65+ participants", YELLOW),
        ("LeetCode: 1850+ solved | peak rating 1819 (MysteriousMortal)",     WHITE),
        ("CodeChef: rank 314 global, Starters 169D (devtrivedi03)",          WHITE),
        ("ICPC 2025: rank 427, Amritapuri Regional (Preliminary)",           WHITE),
    ]
    for i, (msg, col) in enumerate(ITEMS):
        t.gen_text(f"{GRAY}-{RESET} {col}{msg}{RESET}", 6 + i, count=2, contin=True)

    t.gen_text("", 11, count=6, contin=True)
    t.gen_text(get_prompt(), 12, count=15, contin=True)
    t.toggle_show_cursor(True)
    t.gen_text("", 12, count=39, contin=True)


def scene_education(t):
    t.toggle_show_cursor(False)

    t.gen_text(get_prompt(), 2, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text(f"{WHITE}tree ~/education{RESET}", 2, contin=True, speed=1)
    t.toggle_show_cursor(False)
    t.gen_text("", 2, count=5, contin=True)

    t.gen_text(f"{CYAN}education/{RESET}", 4, count=2, contin=True)

    t.gen_text(f"{GRAY}+--{RESET} {YELLOW}Dhirubhai Ambani University{RESET}", 5, count=2, contin=True)
    t.gen_text(f"{GRAY}|   +--{RESET} {CYAN}degree{RESET}      {WHITE}B.Tech, ICT{RESET}", 6, count=2, contin=True)
    t.gen_text(f"{GRAY}|   +--{RESET} {CYAN}period{RESET}      {WHITE}Aug 2023 - Present{RESET}", 7, count=2, contin=True)
    t.gen_text(f"{GRAY}|   +--{RESET} {CYAN}cpi{RESET}         {WHITE}8.59{RESET}", 8, count=2, contin=True)
    t.gen_text(f"{GRAY}|   +--{RESET} {CYAN}coursework{RESET}", 9, count=2, contin=True)
    t.gen_text(f"{GRAY}|       +--{RESET} {WHITE}Object-Oriented Programming{RESET}", 10, count=2, contin=True)
    t.gen_text(f"{GRAY}|       +--{RESET} {WHITE}Data Structures & Algorithms{RESET}", 11, count=2, contin=True)
    t.gen_text(f"{GRAY}|       +--{RESET} {WHITE}DBMS{RESET}", 12, count=2, contin=True)
    t.gen_text(f"{GRAY}|       +--{RESET} {WHITE}Operating Systems{RESET}", 13, count=2, contin=True)
    t.gen_text(f"{GRAY}|       +--{RESET} {WHITE}Computer Networks{RESET}", 14, count=2, contin=True)

    t.gen_text(f"{GRAY}+--{RESET} {YELLOW}Prime Science School (GSHSEB){RESET}", 15, count=2, contin=True)
    t.gen_text(f"{GRAY}|   +--{RESET} {CYAN}jee{RESET}         {WHITE}99.02 percentile{RESET}", 17, count=2, contin=True)
    t.gen_text(f"{GRAY}|   +--{RESET} {CYAN}percentage{RESET}  {WHITE}82.15{RESET}", 16, count=2, contin=True)

    t.gen_text(f"{GRAY}+--{RESET} {YELLOW}Bhavan's Shri A.K. Doshi Vidyalaya (GSEB){RESET}", 18, count=2, contin=True)
    t.gen_text(f"{GRAY}    +--{RESET} {CYAN}percentage{RESET}  {WHITE}86.16{RESET}", 19, count=2, contin=True)

    t.gen_text("", 21, count=6, contin=True)
    t.gen_text(get_prompt(), 22, count=15, contin=True)
    t.toggle_show_cursor(True)
    t.gen_text("", 22, count=39, contin=True)


def scene_exit(t):
    t.toggle_show_cursor(False)

    t.gen_text(get_prompt(), 2, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text(f"{WHITE}sudo reboot now{RESET}", 2, contin=True, speed=1)
    t.toggle_show_cursor(False)
    t.gen_text("", 2, count=8, contin=True)

    t.gen_text(f"{GRAY}Broadcast message from root@DevOS (pts/0):{RESET}", 4, count=5)
    t.gen_text(f"{WHITE}The system is going down for reboot NOW!{RESET}", 5, count=8)
    t.gen_text("", 6, count=4, contin=True)

    t.gen_text(f"{GRAY}Connection to DevOS closed.{RESET}", 8, count=12)
    t.gen_text("", 9, count=4, contin=True)

    t.gen_text(f"{RED}disconnected...{RESET}", 11, count=7)


def main():
    t = gifos.Terminal(750, 400, 15, 15)
    scene_boot(t)
    scene_whoami(t)
    scene_experience(t)
    scene_docker_ps(t)
    scene_inspect_trimium(t)
    scene_inspect_talkasaurus(t)
    scene_skills(t)
    scene_contact(t)
    scene_achievements(t)
    scene_education(t)
    scene_exit(t)
    t.gen_gif()


if __name__ == "__main__":
    main()