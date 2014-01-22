import re
from billy.scrape.actions import Rule, BaseCategorizer

# These are regex patterns that map to action categories.
_categorizer_rules = (
    Rule([u'Amendment #\\S+ \\((?P<legislator>.+?)\\) bundle YES adopted'],
         [u'amendment:passed']),
    Rule([u'(?i)Signed by (the )Governor'], [u'committee:referred']),
    Rule([u'Accompanied (by )?(?P<bill_id>[SH]\\S+)'], []),
    Rule([u'Discharged to the committee on (?P<committees>.+)'],
         [u'committee:referred']),
    Rule([u'(?i)Amendment #\\d+ adopted'], [u'amendment:passed']),
    Rule([u'Amendment #\\d+ \\((?P<legislator>.+?)\\) rejected',
    u'(?i)amendment.+?rejected'],
         [u'amendment:failed']),
    Rule([u'(?is)Amendment \\S+ withdrawn'], [u'amendment:withdrawn']),
    Rule([u'Amendment #\\S+ \\((?P<legislator>.+?)\\) Pending'],
         [u'amendment:introduced']),
    Rule([u'(?P<bill>[HS]\\d+)'], []),
    Rule([u'(?i)Amendment \\(#\\d+\\) adopted'], [u'amendment:passed']),
    Rule([u'(?i)with veto'], [u'governor:vetoed']),
    Rule([u'reported favorably by committee'], [u'committee:passed:favorable']),
    Rule([u'Accompan\\S+ .+?(?P<bill_id>[SH]\\S+)'], []),
    Rule([u'(?i)Amendment \\d+ pending'], [u'amendment:tabled']),
    Rule([u'Read,'], [u'bill:reading:1']),
    Rule([u'(?i)Amendment #\\S+ \\((?P<legislator>.+?)\\)\\s+-\\s+rejected',
    u'(?i)Amendment \\d+ rejected',
    u'Amendment #?\\S+ \\((?P<legislator>.+?)\\) rejected'],
         [u'amendment:failed']),
    Rule([u'Amended \\((?P<legislator>.+?)\\) ',
    u'Amendment #?\\S+ \\((?P<legislator>.+?)\\) adopted'],
         [u'amendment:passed']),
    Rule([u'(?i)read.{,10}second'], [u'bill:reading:2']),
    Rule([u'Amendment #\\d+ \\((?P<legislator>.+?)\\) pending'],
         [u'amendment:introduced']),
    Rule([u'Enacted'], [u'bill:passed']),
    Rule([u'Amendment #\\S+ \\((?P<legislator>.+?)\\) Adopted',
    u'Accompanied a study order, (see )?(?P<bill_id>[SH]\\S+)'],
         []),
    Rule([u'passed over veto'], [u'bill:veto_override:passed']),
    Rule([u'(?i)Read third'], [u'bill:reading:3']),
    Rule([u'Bill Filed'], [u'bill:introduced']),
    Rule([u'(?i)Amendment #\\S+ rejected'], [u'amendment:failed']),
    Rule([u'laid aside'], [u'amendment:tabled']),
    Rule([u'(?i)Amendment \\(#\\d+\\) rejected'], [u'amendment:failed']),
    Rule([u'(?i)amendment.+?adopted'], [u'amendment:passed']),
    Rule([u'Adopted, (see )?(?P<bill_id>[SH]\\S+)'], []),
    Rule([u'(?is)Amendment \\(\\d+\\) rejected'], [u'amendment:failed']),
    Rule([u'(?P<yes_votes>\\d+) YEAS.+?(?P<no_votes>\\d+) NAYS'], []),
    Rule([u'Passed to be engrossed'], [u'bill:passed']),
    Rule([u'Amendment #\\d+ \\((?P<legislator>.+?)\\) adopted'],
         [u'amendment:passed']),
    Rule([u'Amendment #\\S+ \\((?P<legislator>.+?)\\) Rejected'],
         [u'amendment:failed']),
    Rule([u'referred to (?P<committees>.+)'], []),
    Rule([u'Amended by'], [u'amendment:passed']),
    Rule(['Committee recommended ought to pass'], ['committee:passed:favorable']),
    Rule([u'Amendment #\\S+ \\((?P<legislator>.+?)\\) bundle NO rejected'],
         [u'amendment:failed']),
    Rule([u'(?is)Amendment \\(\\d+\\) adopted'], [u'amendment:passed']),
    Rule([u'(?i)(Referred|Recommittedra) to (?P<committees>committee on.+)'],
         [u'committee:referred']),
    Rule([u'Accompanied a new draft, (see )?(?P<bill_id>[SH]\\S+)'], []),
    Rule([u'(?i)Amendment #\\S+ \\((?P<legislator>.+?)\\) bundle NO rejected'],
         [u'amendment:failed']),
    Rule([u'(?i)(Referred|Recommittedra) to (?P<chamber>\\S+) (?P<committees>committee on.+)'],
         [u'committee:referred']),
    Rule(['Committee recommended ought NOT'], ['committee:passed:unfavorable']),
    Rule([u'(?i)(Referred|Recommittedra) (to|from)( the)? (?P<chamber>\\S+) (?P<committees>committee on.+)'],
         [u'committee:referred']),
    Rule([u'(?i)Amendment #\\d+ rejected'], [u'amendment:failed']),
    Rule([u'(?i)Amendment \\d+ adopted'], [u'amendment:passed']),
    Rule([u'Committee of Conference appointed \\((?P<legislator>.+?)\\)'], [])
    )


class Categorizer(BaseCategorizer):
    rules = _categorizer_rules
