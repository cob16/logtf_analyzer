from unittest import TestCase

from logtf_analyser.logs.chatbuilder import ChatBuilder


class TestChatBuilder(TestCase):
    def test_build(self):
        log_id = 123456
        chat_arary = ChatBuilder(log_id, EXMPLE_LOG).build()
        assert len(chat_arary) == 26

        assert chat_arary[0].log_id == log_id
        assert chat_arary[0].user_id == '[U:1:162288532]'
        assert chat_arary[0].username == 'Eternal'
        assert chat_arary[0].msg == 'ur mean'


EXMPLE_LOG = {
    "version": 3,
    "teams": {
        "Red": {
            "score": 3,
            "kills": 124,
            "deaths": 0,
            "dmg": 43155,
            "charges": 6,
            "drops": 1,
            "firstcaps": 4,
            "caps": 16
        },
        "Blue": {
            "score": 3,
            "kills": 122,
            "deaths": 0,
            "dmg": 39794,
            "charges": 8,
            "drops": 1,
            "firstcaps": 3,
            "caps": 14
        }
    },
    "length": 1768,
    "players": {
        "[U:1:355240130]": {
            "team": "Blue",
            "class_stats": [
                {
                    "type": "scout",
                    "kills": 10,
                    "assists": 7,
                    "deaths": 9,
                    "dmg": 2725,
                    "weapon": {
                        "tf_projectile_pipe_remote": {
                            "kills": 0,
                            "dmg": 0,
                            "avg_dmg": 0,
                            "shots": 1,
                            "hits": 0
                        },
                        "scattergun": {
                            "kills": 9,
                            "dmg": 2604,
                            "avg_dmg": 31.75609756097561,
                            "shots": 135,
                            "hits": 81
                        },
                        "pistol_scout": {
                            "kills": 1,
                            "dmg": 121,
                            "avg_dmg": 15.125,
                            "shots": 37,
                            "hits": 8
                        }
                    },
                    "total_time": 773
                },
                {
                    "type": "demoman",
                    "kills": 10,
                    "assists": 2,
                    "deaths": 6,
                    "dmg": 2930,
                    "weapon": {
                        "tf_projectile_pipe_remote": {
                            "kills": 5,
                            "dmg": 2197,
                            "avg_dmg": 47.76086956521739,
                            "shots": 137,
                            "hits": 36
                        },
                        "tf_projectile_pipe": {
                            "kills": 5,
                            "dmg": 733,
                            "avg_dmg": 66.63636363636364,
                            "shots": 62,
                            "hits": 10
                        }
                    },
                    "total_time": 526
                },
                {
                    "type": "sniper",
                    "kills": 5,
                    "assists": 0,
                    "deaths": 7,
                    "dmg": 1005,
                    "weapon": {
                        "sniperrifle": {
                            "kills": 5,
                            "dmg": 1005,
                            "avg_dmg": 125.625,
                            "shots": 22,
                            "hits": 8
                        }
                    },
                    "total_time": 289
                },
                {
                    "type": "engineer",
                    "kills": 5,
                    "assists": 0,
                    "deaths": 1,
                    "dmg": 565,
                    "weapon": {
                        "obj_sentrygun": {
                            "kills": 0,
                            "dmg": 161,
                            "avg_dmg": 17.88888888888889,
                            "shots": 0,
                            "hits": 0
                        },
                        "shotgun_primary": {
                            "kills": 4,
                            "dmg": 231,
                            "avg_dmg": 33,
                            "shots": 8,
                            "hits": 6
                        },
                        "obj_sentrygun2": {
                            "kills": 0,
                            "dmg": 80,
                            "avg_dmg": 16,
                            "shots": 0,
                            "hits": 0
                        },
                        "pistol": {
                            "kills": 0,
                            "dmg": 13,
                            "avg_dmg": 13,
                            "shots": 19,
                            "hits": 1
                        },
                        "obj_sentrygun3": {
                            "kills": 1,
                            "dmg": 80,
                            "avg_dmg": 16,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 89
                },
                {
                    "type": "heavyweapons",
                    "kills": 4,
                    "assists": 0,
                    "deaths": 1,
                    "dmg": 816,
                    "weapon": {
                        "tomislav": {
                            "kills": 4,
                            "dmg": 816,
                            "avg_dmg": 17,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 88
                }
            ],
            "kills": 34,
            "deaths": 24,
            "assists": 9,
            "suicides": 0,
            "kapd": "1.8",
            "kpd": "1.4",
            "dmg": 8041,
            "dmg_real": 1101,
            "dt": 7881,
            "dt_real": 770,
            "hr": 3646,
            "lks": 5,
            "as": 0,
            "dapd": 335,
            "dapm": 272,
            "ubers": 0,
            "ubertypes": {},
            "drops": 0,
            "medkits": 42,
            "medkits_hp": 1286,
            "backstabs": 0,
            "headshots": 4,
            "headshots_hit": 6,
            "sentries": 0,
            "heal": 0,
            "cpc": 5,
            "ic": 0
        },
        "[U:1:162288532]": {
            "team": "Blue",
            "class_stats": [
                {
                    "type": "soldier",
                    "kills": 23,
                    "assists": 14,
                    "deaths": 29,
                    "dmg": 7880,
                    "weapon": {
                        "tf_projectile_rocket": {
                            "kills": 21,
                            "dmg": 7880,
                            "avg_dmg": 67.35042735042735,
                            "shots": 223,
                            "hits": 105
                        },
                        "world": {
                            "kills": 2,
                            "dmg": 0,
                            "avg_dmg": 0,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 1768
                }
            ],
            "kills": 23,
            "deaths": 29,
            "assists": 14,
            "suicides": 0,
            "kapd": "1.3",
            "kpd": "0.8",
            "dmg": 7880,
            "dmg_real": 703,
            "dt": 7054,
            "dt_real": 1065,
            "hr": 2674,
            "lks": 4,
            "as": 4,
            "dapd": 271,
            "dapm": 267,
            "ubers": 0,
            "ubertypes": {},
            "drops": 0,
            "medkits": 44,
            "medkits_hp": 1882,
            "backstabs": 0,
            "headshots": 0,
            "headshots_hit": 0,
            "sentries": 0,
            "heal": 0,
            "cpc": 1,
            "ic": 0
        },
        "[U:1:96727704]": {
            "team": "Red",
            "class_stats": [
                {
                    "type": "scout",
                    "kills": 32,
                    "assists": 7,
                    "deaths": 23,
                    "dmg": 7792,
                    "weapon": {
                        "scattergun": {
                            "kills": 28,
                            "dmg": 7436,
                            "avg_dmg": 27.43911439114391,
                            "shots": 391,
                            "hits": 244
                        },
                        "maxgun": {
                            "kills": 3,
                            "dmg": 356,
                            "avg_dmg": 15.478260869565217,
                            "shots": 98,
                            "hits": 23
                        },
                        "world": {
                            "kills": 1,
                            "dmg": 0,
                            "avg_dmg": 0,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 1544
                },
                {
                    "type": "sniper",
                    "kills": 1,
                    "assists": 1,
                    "deaths": 2,
                    "dmg": 551,
                    "weapon": {
                        "sniperrifle": {
                            "kills": 1,
                            "dmg": 551,
                            "avg_dmg": 110.2,
                            "shots": 17,
                            "hits": 5
                        }
                    },
                    "total_time": 224
                }
            ],
            "kills": 33,
            "deaths": 25,
            "assists": 8,
            "suicides": 0,
            "kapd": "1.6",
            "kpd": "1.3",
            "dmg": 8343,
            "dmg_real": 886,
            "dt": 5828,
            "dt_real": 1035,
            "hr": 2306,
            "lks": 6,
            "as": 0,
            "dapd": 333,
            "dapm": 283,
            "ubers": 0,
            "ubertypes": {},
            "drops": 0,
            "medkits": 32,
            "medkits_hp": 798,
            "backstabs": 0,
            "headshots": 1,
            "headshots_hit": 2,
            "sentries": 0,
            "heal": 0,
            "cpc": 0,
            "ic": 0
        },
        "[U:1:321959931]": {
            "team": "Red",
            "class_stats": [
                {
                    "type": "scout",
                    "kills": 11,
                    "assists": 6,
                    "deaths": 23,
                    "dmg": 2736,
                    "weapon": {
                        "scattergun": {
                            "kills": 8,
                            "dmg": 2595,
                            "avg_dmg": 24.714285714285715,
                            "shots": 193,
                            "hits": 90
                        },
                        "pistol_scout": {
                            "kills": 2,
                            "dmg": 106,
                            "avg_dmg": 17.666666666666668,
                            "shots": 67,
                            "hits": 6
                        },
                        "bat": {
                            "kills": 1,
                            "dmg": 35,
                            "avg_dmg": 35,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 1462
                },
                {
                    "type": "pyro",
                    "kills": 2,
                    "assists": 0,
                    "deaths": 3,
                    "dmg": 335,
                    "weapon": {
                        "backburner": {
                            "kills": 1,
                            "dmg": 187,
                            "avg_dmg": 4.675,
                            "shots": 0,
                            "hits": 0
                        },
                        "tf_projectile_rocket": {
                            "kills": 0,
                            "dmg": 148,
                            "avg_dmg": 148,
                            "shots": 0,
                            "hits": 0
                        },
                        "deflect_rocket": {
                            "kills": 1,
                            "dmg": 0,
                            "avg_dmg": 0,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 162
                },
                {
                    "type": "spy",
                    "kills": 0,
                    "assists": 0,
                    "deaths": 1,
                    "dmg": 0,
                    "weapon": {},
                    "total_time": 96
                },
                {
                    "type": "heavyweapons",
                    "kills": 0,
                    "assists": 0,
                    "deaths": 1,
                    "dmg": 25,
                    "weapon": {
                        "long_heatmaker": {
                            "kills": 0,
                            "dmg": 25,
                            "avg_dmg": 6.25,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 48
                }
            ],
            "kills": 13,
            "deaths": 28,
            "assists": 6,
            "suicides": 1,
            "kapd": "0.7",
            "kpd": "0.5",
            "dmg": 3096,
            "dmg_real": 514,
            "dt": 6194,
            "dt_real": 967,
            "hr": 1677,
            "lks": 3,
            "as": 0,
            "dapd": 110,
            "dapm": 105,
            "ubers": 0,
            "ubertypes": {},
            "drops": 0,
            "medkits": 29,
            "medkits_hp": 611,
            "backstabs": 0,
            "headshots": 0,
            "headshots_hit": 0,
            "sentries": 0,
            "heal": 0,
            "cpc": 12,
            "ic": 0
        },
        "[U:1:84854265]": {
            "team": "Red",
            "class_stats": [
                {
                    "type": "demoman",
                    "kills": 20,
                    "assists": 5,
                    "deaths": 17,
                    "dmg": 11630,
                    "weapon": {
                        "tf_projectile_pipe_remote": {
                            "kills": 6,
                            "dmg": 7114,
                            "avg_dmg": 55.578125,
                            "shots": 429,
                            "hits": 111
                        },
                        "tf_projectile_pipe": {
                            "kills": 13,
                            "dmg": 4516,
                            "avg_dmg": 72.83870967741936,
                            "shots": 173,
                            "hits": 53
                        },
                        "world": {
                            "kills": 1,
                            "dmg": 0,
                            "avg_dmg": 0,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 1767
                }
            ],
            "kills": 20,
            "deaths": 17,
            "assists": 5,
            "suicides": 0,
            "kapd": "1.5",
            "kpd": "1.2",
            "dmg": 11630,
            "dmg_real": 942,
            "dt": 10586,
            "dt_real": 782,
            "hr": 9356,
            "lks": 4,
            "as": 4,
            "dapd": 684,
            "dapm": 394,
            "ubers": 0,
            "ubertypes": {},
            "drops": 0,
            "medkits": 56,
            "medkits_hp": 1975,
            "backstabs": 0,
            "headshots": 0,
            "headshots_hit": 0,
            "sentries": 0,
            "heal": 0,
            "cpc": 1,
            "ic": 0
        },
        "[U:1:88031169]": {
            "team": "Blue",
            "class_stats": [
                {
                    "type": "medic",
                    "kills": 3,
                    "assists": 6,
                    "deaths": 14,
                    "dmg": 651,
                    "weapon": {
                        "crusaders_crossbow": {
                            "kills": 1,
                            "dmg": 238,
                            "avg_dmg": 47.6,
                            "shots": 118,
                            "hits": 59
                        },
                        "ubersaw": {
                            "kills": 2,
                            "dmg": 413,
                            "avg_dmg": 68.83333333333333,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 1768
                }
            ],
            "kills": 3,
            "deaths": 14,
            "assists": 6,
            "suicides": 0,
            "kapd": "0.6",
            "kpd": "0.2",
            "dmg": 651,
            "dmg_real": 139,
            "dt": 5201,
            "dt_real": 536,
            "hr": 0,
            "lks": 1,
            "as": 0,
            "dapd": 46,
            "dapm": 22,
            "ubers": 8,
            "ubertypes": {
                "medigun": 8
            },
            "drops": 1,
            "medkits": 10,
            "medkits_hp": 324,
            "backstabs": 0,
            "headshots": 0,
            "headshots_hit": 0,
            "sentries": 0,
            "heal": 25894,
            "cpc": 1,
            "ic": 0,
            "medicstats": {
                "advantages_lost": 3,
                "biggest_advantage_lost": 11,
                "deaths_with_95_99_uber": 0,
                "deaths_within_20s_after_uber": 2,
                "avg_time_before_healing": 4.699999999999999,
                "avg_time_to_build": 53.4,
                "avg_time_before_using": 39.125,
                "avg_uber_length": 7.328571428571427
            }
        },
        "[U:1:102670289]": {
            "team": "Blue",
            "class_stats": [
                {
                    "type": "soldier",
                    "kills": 15,
                    "assists": 9,
                    "deaths": 17,
                    "dmg": 8574,
                    "weapon": {
                        "tf_projectile_rocket": {
                            "kills": 15,
                            "dmg": 8574,
                            "avg_dmg": 49.5606936416185,
                            "shots": 345,
                            "hits": 151
                        }
                    },
                    "total_time": 1736
                },
                {
                    "type": "sniper",
                    "kills": 0,
                    "assists": 0,
                    "deaths": 1,
                    "dmg": 0,
                    "weapon": {
                        "machina": {
                            "kills": 0,
                            "dmg": 0,
                            "avg_dmg": 0,
                            "shots": 1,
                            "hits": 0
                        }
                    },
                    "total_time": 32
                }
            ],
            "kills": 15,
            "deaths": 18,
            "assists": 9,
            "suicides": 0,
            "kapd": "1.3",
            "kpd": "0.8",
            "dmg": 8574,
            "dmg_real": 547,
            "dt": 10396,
            "dt_real": 924,
            "hr": 10204,
            "lks": 3,
            "as": 0,
            "dapd": 476,
            "dapm": 290,
            "ubers": 0,
            "ubertypes": {},
            "drops": 0,
            "medkits": 17,
            "medkits_hp": 619,
            "backstabs": 0,
            "headshots": 0,
            "headshots_hit": 0,
            "sentries": 0,
            "heal": 0,
            "cpc": 4,
            "ic": 0
        },
        "[U:1:119246276]": {
            "team": "Red",
            "class_stats": [
                {
                    "type": "soldier",
                    "kills": 19,
                    "assists": 9,
                    "deaths": 19,
                    "dmg": 7776,
                    "weapon": {
                        "tf_projectile_rocket": {
                            "kills": 11,
                            "dmg": 5950,
                            "avg_dmg": 57.76699029126213,
                            "shots": 201,
                            "hits": 90
                        },
                        "shotgun_soldier": {
                            "kills": 3,
                            "dmg": 844,
                            "avg_dmg": 30.142857142857142,
                            "shots": 39,
                            "hits": 28
                        },
                        "unique_pickaxe_escape": {
                            "kills": 0,
                            "dmg": 130,
                            "avg_dmg": 65,
                            "shots": 0,
                            "hits": 0
                        },
                        "rocketlauncher_directhit": {
                            "kills": 1,
                            "dmg": 409,
                            "avg_dmg": 136.33333333333334,
                            "shots": 12,
                            "hits": 3
                        },
                        "liberty_launcher": {
                            "kills": 3,
                            "dmg": 363,
                            "avg_dmg": 60.5,
                            "shots": 7,
                            "hits": 6
                        },
                        "quake_rl": {
                            "kills": 0,
                            "dmg": 80,
                            "avg_dmg": 40,
                            "shots": 8,
                            "hits": 2
                        },
                        "world": {
                            "kills": 1,
                            "dmg": 0,
                            "avg_dmg": 0,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 1426
                },
                {
                    "type": "spy",
                    "kills": 1,
                    "assists": 0,
                    "deaths": 4,
                    "dmg": 566,
                    "weapon": {
                        "ambassador": {
                            "kills": 0,
                            "dmg": 36,
                            "avg_dmg": 18,
                            "shots": 5,
                            "hits": 2
                        },
                        "big_earner": {
                            "kills": 1,
                            "dmg": 530,
                            "avg_dmg": 176.66666666666666,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 193
                },
                {
                    "type": "engineer",
                    "kills": 1,
                    "assists": 1,
                    "deaths": 1,
                    "dmg": 218,
                    "weapon": {
                        "shotgun_primary": {
                            "kills": 0,
                            "dmg": 23,
                            "avg_dmg": 5.75,
                            "shots": 3,
                            "hits": 2
                        },
                        "eureka_effect": {
                            "kills": 1,
                            "dmg": 195,
                            "avg_dmg": 65,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 109
                },
                {
                    "type": "sniper",
                    "kills": 0,
                    "assists": 0,
                    "deaths": 1,
                    "dmg": 0,
                    "weapon": {
                        "sniperrifle": {
                            "kills": 0,
                            "dmg": 0,
                            "avg_dmg": 0,
                            "shots": 2,
                            "hits": 0
                        }
                    },
                    "total_time": 40
                }
            ],
            "kills": 21,
            "deaths": 25,
            "assists": 10,
            "suicides": 1,
            "kapd": "1.2",
            "kpd": "0.8",
            "dmg": 8560,
            "dmg_real": 1074,
            "dt": 6546,
            "dt_real": 708,
            "hr": 4828,
            "lks": 2,
            "as": 0,
            "dapd": 342,
            "dapm": 290,
            "ubers": 0,
            "ubertypes": {},
            "drops": 0,
            "medkits": 57,
            "medkits_hp": 2098,
            "backstabs": 1,
            "headshots": 0,
            "headshots_hit": 0,
            "sentries": 0,
            "heal": 0,
            "cpc": 1,
            "ic": 0
        },
        "[U:1:108763985]": {
            "team": "Red",
            "class_stats": [
                {
                    "type": "soldier",
                    "kills": 36,
                    "assists": 11,
                    "deaths": 17,
                    "dmg": 10800,
                    "weapon": {
                        "tf_projectile_rocket": {
                            "kills": 34,
                            "dmg": 10800,
                            "avg_dmg": 60.33519553072626,
                            "shots": 314,
                            "hits": 161
                        },
                        "world": {
                            "kills": 2,
                            "dmg": 0,
                            "avg_dmg": 0,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 1768
                }
            ],
            "kills": 36,
            "deaths": 17,
            "assists": 11,
            "suicides": 0,
            "kapd": "2.8",
            "kpd": "2.1",
            "dmg": 10800,
            "dmg_real": 1332,
            "dt": 6639,
            "dt_real": 449,
            "hr": 4589,
            "lks": 7,
            "as": 2,
            "dapd": 635,
            "dapm": 366,
            "ubers": 0,
            "ubertypes": {},
            "drops": 0,
            "medkits": 94,
            "medkits_hp": 3097,
            "backstabs": 0,
            "headshots": 0,
            "headshots_hit": 0,
            "sentries": 0,
            "heal": 0,
            "cpc": 4,
            "ic": 0
        },
        "[U:1:167882722]": {
            "team": "Red",
            "class_stats": [
                {
                    "type": "medic",
                    "kills": 1,
                    "assists": 10,
                    "deaths": 12,
                    "dmg": 726,
                    "weapon": {
                        "crusaders_crossbow": {
                            "kills": 1,
                            "dmg": 661,
                            "avg_dmg": 55.083333333333336,
                            "shots": 198,
                            "hits": 78
                        },
                        "ubersaw": {
                            "kills": 0,
                            "dmg": 65,
                            "avg_dmg": 65,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 1768
                }
            ],
            "kills": 1,
            "deaths": 12,
            "assists": 10,
            "suicides": 0,
            "kapd": "0.9",
            "kpd": "0.1",
            "dmg": 726,
            "dmg_real": 8,
            "dt": 4001,
            "dt_real": 440,
            "hr": 0,
            "lks": 1,
            "as": 0,
            "dapd": 60,
            "dapm": 24,
            "ubers": 6,
            "ubertypes": {
                "medigun": 6
            },
            "drops": 1,
            "medkits": 8,
            "medkits_hp": 271,
            "backstabs": 0,
            "headshots": 0,
            "headshots_hit": 0,
            "sentries": 0,
            "heal": 22705,
            "cpc": 3,
            "ic": 0,
            "medicstats": {
                "advantages_lost": 1,
                "biggest_advantage_lost": 25,
                "deaths_with_95_99_uber": 0,
                "deaths_within_20s_after_uber": 2,
                "avg_time_before_healing": 6.655555555555555,
                "avg_time_to_build": 75.125,
                "avg_time_before_using": 33,
                "avg_uber_length": 7.333333333333333
            }
        },
        "[U:1:102992936]": {
            "team": "Blue",
            "class_stats": [
                {
                    "type": "demoman",
                    "kills": 13,
                    "assists": 7,
                    "deaths": 9,
                    "dmg": 5913,
                    "weapon": {
                        "tf_projectile_pipe_remote": {
                            "kills": 7,
                            "dmg": 3261,
                            "avg_dmg": 54.35,
                            "shots": 299,
                            "hits": 57
                        },
                        "tf_projectile_pipe": {
                            "kills": 6,
                            "dmg": 2652,
                            "avg_dmg": 78,
                            "shots": 194,
                            "hits": 31
                        }
                    },
                    "total_time": 1241
                },
                {
                    "type": "scout",
                    "kills": 4,
                    "assists": 2,
                    "deaths": 7,
                    "dmg": 1687,
                    "weapon": {
                        "scattergun": {
                            "kills": 1,
                            "dmg": 1342,
                            "avg_dmg": 23.964285714285715,
                            "shots": 79,
                            "hits": 52
                        },
                        "pistol_scout": {
                            "kills": 3,
                            "dmg": 345,
                            "avg_dmg": 13.8,
                            "shots": 131,
                            "hits": 25
                        }
                    },
                    "total_time": 453
                },
                {
                    "type": "sniper",
                    "kills": 0,
                    "assists": 0,
                    "deaths": 0,
                    "dmg": 500,
                    "weapon": {
                        "sniperrifle": {
                            "kills": 0,
                            "dmg": 500,
                            "avg_dmg": 125,
                            "shots": 8,
                            "hits": 4
                        }
                    },
                    "total_time": 64
                }
            ],
            "kills": 17,
            "deaths": 16,
            "assists": 9,
            "suicides": 0,
            "kapd": "1.6",
            "kpd": "1.1",
            "dmg": 8100,
            "dmg_real": 682,
            "dt": 6255,
            "dt_real": 667,
            "hr": 6159,
            "lks": 8,
            "as": 1,
            "dapd": 506,
            "dapm": 274,
            "ubers": 0,
            "ubertypes": {},
            "drops": 0,
            "medkits": 29,
            "medkits_hp": 911,
            "backstabs": 0,
            "headshots": 0,
            "headshots_hit": 3,
            "sentries": 0,
            "heal": 0,
            "cpc": 3,
            "ic": 0
        },
        "[U:1:125148025]": {
            "team": "Blue",
            "class_stats": [
                {
                    "type": "scout",
                    "kills": 29,
                    "assists": 6,
                    "deaths": 20,
                    "dmg": 5843,
                    "weapon": {
                        "maxgun": {
                            "kills": 5,
                            "dmg": 185,
                            "avg_dmg": 16.818181818181817,
                            "shots": 68,
                            "hits": 11
                        },
                        "scattergun": {
                            "kills": 23,
                            "dmg": 5658,
                            "avg_dmg": 24.6,
                            "shots": 377,
                            "hits": 204
                        },
                        "world": {
                            "kills": 1,
                            "dmg": 0,
                            "avg_dmg": 0,
                            "shots": 0,
                            "hits": 0
                        }
                    },
                    "total_time": 1601
                },
                {
                    "type": "sniper",
                    "kills": 1,
                    "assists": 0,
                    "deaths": 3,
                    "dmg": 705,
                    "weapon": {
                        "sniperrifle": {
                            "kills": 1,
                            "dmg": 705,
                            "avg_dmg": 176.25,
                            "shots": 14,
                            "hits": 4
                        }
                    },
                    "total_time": 167
                }
            ],
            "kills": 30,
            "deaths": 23,
            "assists": 6,
            "suicides": 0,
            "kapd": "1.6",
            "kpd": "1.3",
            "dmg": 6548,
            "dmg_real": 1209,
            "dt": 6368,
            "dt_real": 794,
            "hr": 3160,
            "lks": 5,
            "as": 0,
            "dapd": 284,
            "dapm": 222,
            "ubers": 0,
            "ubertypes": {},
            "drops": 0,
            "medkits": 31,
            "medkits_hp": 725,
            "backstabs": 0,
            "headshots": 1,
            "headshots_hit": 2,
            "sentries": 0,
            "heal": 0,
            "cpc": 6,
            "ic": 0
        }
    },
    "names": {
        "[U:1:355240130]": "jjjjaaack",
        "[U:1:162288532]": "Eternal",
        "[U:1:96727704]": "Yop.",
        "[U:1:321959931]": "LZER",
        "[U:1:84854265]": "+ai",
        "[U:1:88031169]": "jsabb",
        "[U:1:102670289]": "FeedbackLoop",
        "[U:1:119246276]": "my nama swag",
        "[U:1:108763985]": "emgee",
        "[U:1:167882722]": "choppy",
        "[U:1:102992936]": "Tesla",
        "[U:1:125148025]": "chezs"
    },
    "rounds": [
        {
            "start_time": 1507318225,
            "winner": "Red",
            "team": {
                "Blue": {
                    "score": 0,
                    "kills": 23,
                    "dmg": 9852,
                    "ubers": 2
                },
                "Red": {
                    "score": 1,
                    "kills": 33,
                    "dmg": 11055,
                    "ubers": 2
                }
            },
            "events": [
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 74,
                    "steamid": "[U:1:167882722]",
                    "team": "Red"
                },
                {
                    "type": "medic_death",
                    "time": 85,
                    "team": "Red",
                    "steamid": "[U:1:167882722]",
                    "killer": "[U:1:162288532]"
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 88,
                    "steamid": "[U:1:88031169]",
                    "team": "Blue"
                },
                {
                    "type": "medic_death",
                    "time": 108,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:96727704]"
                },
                {
                    "type": "pointcap",
                    "time": 119,
                    "team": "Blue",
                    "point": 3
                },
                {
                    "type": "medic_death",
                    "time": 168,
                    "team": "Red",
                    "steamid": "[U:1:167882722]",
                    "killer": "[U:1:102670289]"
                },
                {
                    "type": "medic_death",
                    "time": 177,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:321959931]"
                },
                {
                    "type": "pointcap",
                    "time": 207,
                    "team": "Red",
                    "point": 3
                },
                {
                    "type": "pointcap",
                    "time": 232,
                    "team": "Red",
                    "point": 2
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 307,
                    "steamid": "[U:1:167882722]",
                    "team": "Red"
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 313,
                    "steamid": "[U:1:88031169]",
                    "team": "Blue"
                },
                {
                    "type": "medic_death",
                    "time": 342,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:119246276]"
                },
                {
                    "type": "medic_death",
                    "time": 347,
                    "team": "Red",
                    "steamid": "[U:1:167882722]",
                    "killer": "[U:1:355240130]"
                },
                {
                    "type": "medic_death",
                    "time": 398,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:119246276]"
                },
                {
                    "type": "pointcap",
                    "time": 418,
                    "team": "Red",
                    "point": 1
                },
                {
                    "type": "round_win",
                    "time": 418,
                    "team": "Red"
                }
            ],
            "players": {
                "[U:1:96727704]": {
                    "team": "Red",
                    "kills": 10,
                    "dmg": 2263
                },
                "[U:1:102992936]": {
                    "team": "Blue",
                    "kills": 3,
                    "dmg": 1897
                },
                "[U:1:108763985]": {
                    "team": "Red",
                    "kills": 6,
                    "dmg": 2732
                },
                "[U:1:125148025]": {
                    "team": "Blue",
                    "kills": 7,
                    "dmg": 1715
                },
                "[U:1:119246276]": {
                    "team": "Red",
                    "kills": 6,
                    "dmg": 2677
                },
                "[U:1:84854265]": {
                    "team": "Red",
                    "kills": 5,
                    "dmg": 2680
                },
                "[U:1:162288532]": {
                    "team": "Blue",
                    "kills": 3,
                    "dmg": 1357
                },
                "[U:1:102670289]": {
                    "team": "Blue",
                    "kills": 1,
                    "dmg": 2135
                },
                "[U:1:321959931]": {
                    "team": "Red",
                    "kills": 5,
                    "dmg": 542
                },
                "[U:1:355240130]": {
                    "team": "Blue",
                    "kills": 9,
                    "dmg": 2683
                },
                "[U:1:88031169]": {
                    "team": "Blue",
                    "kills": 0,
                    "dmg": 65
                },
                "[U:1:167882722]": {
                    "team": "Red",
                    "kills": 1,
                    "dmg": 161
                },
                "[U:1:87283349]": {
                    "team": None,
                    "kills": 0,
                    "dmg": 0
                }
            },
            "firstcap": "Blue",
            "length": 418
        },
        {
            "start_time": 1507318648,
            "winner": "Blue",
            "team": {
                "Blue": {
                    "score": 1,
                    "kills": 17,
                    "dmg": 3867,
                    "ubers": 1
                },
                "Red": {
                    "score": 1,
                    "kills": 11,
                    "dmg": 3749,
                    "ubers": 0
                }
            },
            "events": [
                {
                    "type": "medic_death",
                    "time": 452,
                    "team": "Red",
                    "steamid": "[U:1:167882722]",
                    "killer": "[U:1:162288532]"
                },
                {
                    "type": "medic_death",
                    "time": 459,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:108763985]"
                },
                {
                    "type": "pointcap",
                    "time": 472,
                    "team": "Blue",
                    "point": 3
                },
                {
                    "type": "pointcap",
                    "time": 520,
                    "team": "Blue",
                    "point": 4
                },
                {
                    "type": "pointcap",
                    "time": 541,
                    "team": "Red",
                    "point": 4
                },
                {
                    "type": "medic_death",
                    "time": 546,
                    "team": "Red",
                    "steamid": "[U:1:167882722]",
                    "killer": "[U:1:162288532]"
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 562,
                    "steamid": "[U:1:88031169]",
                    "team": "Blue"
                },
                {
                    "type": "pointcap",
                    "time": 569,
                    "team": "Blue",
                    "point": 4
                },
                {
                    "type": "medic_death",
                    "time": 571,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:96727704]"
                },
                {
                    "type": "pointcap",
                    "time": 589,
                    "team": "Blue",
                    "point": 5
                },
                {
                    "type": "round_win",
                    "time": 589,
                    "team": "Blue"
                }
            ],
            "players": {
                "[U:1:96727704]": {
                    "team": "Red",
                    "kills": 3,
                    "dmg": 707
                },
                "[U:1:125148025]": {
                    "team": "Blue",
                    "kills": 4,
                    "dmg": 737
                },
                "[U:1:321959931]": {
                    "team": "Red",
                    "kills": 2,
                    "dmg": 339
                },
                "[U:1:119246276]": {
                    "team": "Red",
                    "kills": 4,
                    "dmg": 1191
                },
                "[U:1:102992936]": {
                    "team": "Blue",
                    "kills": 2,
                    "dmg": 590
                },
                "[U:1:84854265]": {
                    "team": "Red",
                    "kills": 0,
                    "dmg": 756
                },
                "[U:1:102670289]": {
                    "team": "Blue",
                    "kills": 2,
                    "dmg": 723
                },
                "[U:1:162288532]": {
                    "team": "Blue",
                    "kills": 6,
                    "dmg": 1235
                },
                "[U:1:355240130]": {
                    "team": "Blue",
                    "kills": 2,
                    "dmg": 387
                },
                "[U:1:108763985]": {
                    "team": "Red",
                    "kills": 2,
                    "dmg": 756
                },
                "[U:1:88031169]": {
                    "team": "Blue",
                    "kills": 1,
                    "dmg": 195
                },
                "[U:1:167882722]": {
                    "team": "Red",
                    "kills": 0,
                    "dmg": 0
                },
                "[U:1:87283349]": {
                    "team": None,
                    "kills": 0,
                    "dmg": 0
                }
            },
            "firstcap": "Blue",
            "length": 166
        },
        {
            "start_time": 1507318819,
            "winner": "Red",
            "team": {
                "Blue": {
                    "score": 1,
                    "kills": 9,
                    "dmg": 3300,
                    "ubers": 0
                },
                "Red": {
                    "score": 2,
                    "kills": 16,
                    "dmg": 4603,
                    "ubers": 1
                }
            },
            "events": [
                {
                    "type": "medic_death",
                    "time": 628,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:108763985]"
                },
                {
                    "type": "medic_death",
                    "time": 636,
                    "team": "Red",
                    "steamid": "[U:1:167882722]",
                    "killer": "[U:1:102670289]"
                },
                {
                    "type": "pointcap",
                    "time": 644,
                    "team": "Red",
                    "point": 3
                },
                {
                    "type": "pointcap",
                    "time": 661,
                    "team": "Red",
                    "point": 2
                },
                {
                    "type": "drop",
                    "time": 751,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]"
                },
                {
                    "type": "medic_death",
                    "time": 751,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:96727704]"
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 755,
                    "steamid": "[U:1:167882722]",
                    "team": "Red"
                },
                {
                    "type": "pointcap",
                    "time": 768,
                    "team": "Red",
                    "point": 1
                },
                {
                    "type": "round_win",
                    "time": 768,
                    "team": "Red"
                }
            ],
            "players": {
                "[U:1:102992936]": {
                    "team": "Blue",
                    "kills": 0,
                    "dmg": 858
                },
                "[U:1:355240130]": {
                    "team": "Blue",
                    "kills": 0,
                    "dmg": 128
                },
                "[U:1:108763985]": {
                    "team": "Red",
                    "kills": 8,
                    "dmg": 1154
                },
                "[U:1:96727704]": {
                    "team": "Red",
                    "kills": 2,
                    "dmg": 866
                },
                "[U:1:84854265]": {
                    "team": "Red",
                    "kills": 4,
                    "dmg": 1602
                },
                "[U:1:321959931]": {
                    "team": "Red",
                    "kills": 0,
                    "dmg": 198
                },
                "[U:1:125148025]": {
                    "team": "Blue",
                    "kills": 4,
                    "dmg": 682
                },
                "[U:1:119246276]": {
                    "team": "Red",
                    "kills": 2,
                    "dmg": 783
                },
                "[U:1:102670289]": {
                    "team": "Blue",
                    "kills": 2,
                    "dmg": 714
                },
                "[U:1:162288532]": {
                    "team": "Blue",
                    "kills": 3,
                    "dmg": 918
                },
                "[U:1:88031169]": {
                    "team": "Blue",
                    "kills": 0,
                    "dmg": 0
                },
                "[U:1:167882722]": {
                    "team": "Red",
                    "kills": 0,
                    "dmg": 0
                },
                "[U:1:87283349]": {
                    "team": None,
                    "kills": 0,
                    "dmg": 0
                }
            },
            "firstcap": "Red",
            "length": 174
        },
        {
            "start_time": 1507318998,
            "winner": "Red",
            "team": {
                "Blue": {
                    "score": 1,
                    "kills": 24,
                    "dmg": 7136,
                    "ubers": 1
                },
                "Red": {
                    "score": 3,
                    "kills": 19,
                    "dmg": 7680,
                    "ubers": 1
                }
            },
            "events": [
                {
                    "type": "medic_death",
                    "time": 799,
                    "team": "Red",
                    "steamid": "[U:1:167882722]",
                    "killer": "[U:1:162288532]"
                },
                {
                    "type": "medic_death",
                    "time": 805,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:108763985]"
                },
                {
                    "type": "pointcap",
                    "time": 828,
                    "team": "Red",
                    "point": 3
                },
                {
                    "type": "pointcap",
                    "time": 846,
                    "team": "Red",
                    "point": 2
                },
                {
                    "type": "medic_death",
                    "time": 866,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:108763985]"
                },
                {
                    "type": "pointcap",
                    "time": 887,
                    "team": "Blue",
                    "point": 2
                },
                {
                    "type": "pointcap",
                    "time": 936,
                    "team": "Red",
                    "point": 2
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 961,
                    "steamid": "[U:1:167882722]",
                    "team": "Red"
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 971,
                    "steamid": "[U:1:88031169]",
                    "team": "Blue"
                },
                {
                    "type": "pointcap",
                    "time": 990,
                    "team": "Blue",
                    "point": 2
                },
                {
                    "type": "pointcap",
                    "time": 1050,
                    "team": "Red",
                    "point": 2
                },
                {
                    "type": "medic_death",
                    "time": 1094,
                    "team": "Red",
                    "steamid": "[U:1:167882722]",
                    "killer": "[U:1:125148025]"
                },
                {
                    "type": "pointcap",
                    "time": 1104,
                    "team": "Red",
                    "point": 1
                },
                {
                    "type": "round_win",
                    "time": 1104,
                    "team": "Red"
                }
            ],
            "players": {
                "[U:1:355240130]": {
                    "team": "Blue",
                    "kills": 6,
                    "dmg": 1423
                },
                "[U:1:102992936]": {
                    "team": "Blue",
                    "kills": 4,
                    "dmg": 1253
                },
                "[U:1:125148025]": {
                    "team": "Blue",
                    "kills": 8,
                    "dmg": 1273
                },
                "[U:1:96727704]": {
                    "team": "Red",
                    "kills": 3,
                    "dmg": 1056
                },
                "[U:1:321959931]": {
                    "team": "Red",
                    "kills": 1,
                    "dmg": 502
                },
                "[U:1:84854265]": {
                    "team": "Red",
                    "kills": 2,
                    "dmg": 1925
                },
                "[U:1:162288532]": {
                    "team": "Blue",
                    "kills": 3,
                    "dmg": 1198
                },
                "[U:1:119246276]": {
                    "team": "Red",
                    "kills": 3,
                    "dmg": 1666
                },
                "[U:1:102670289]": {
                    "team": "Blue",
                    "kills": 3,
                    "dmg": 1914
                },
                "[U:1:88031169]": {
                    "team": "Blue",
                    "kills": 0,
                    "dmg": 75
                },
                "[U:1:108763985]": {
                    "team": "Red",
                    "kills": 10,
                    "dmg": 2240
                },
                "[U:1:167882722]": {
                    "team": "Red",
                    "kills": 0,
                    "dmg": 291
                },
                "[U:1:87283349]": {
                    "team": None,
                    "kills": 0,
                    "dmg": 0
                }
            },
            "firstcap": "Red",
            "length": 331
        },
        {
            "start_time": 1507319334,
            "winner": "Blue",
            "team": {
                "Blue": {
                    "score": 2,
                    "kills": 26,
                    "dmg": 8783,
                    "ubers": 2
                },
                "Red": {
                    "score": 3,
                    "kills": 19,
                    "dmg": 8597,
                    "ubers": 2
                }
            },
            "events": [
                {
                    "type": "pointcap",
                    "time": 1216,
                    "team": "Red",
                    "point": 3
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 1244,
                    "steamid": "[U:1:88031169]",
                    "team": "Blue"
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 1246,
                    "steamid": "[U:1:167882722]",
                    "team": "Red"
                },
                {
                    "type": "medic_death",
                    "time": 1260,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:84854265]"
                },
                {
                    "type": "pointcap",
                    "time": 1275,
                    "team": "Red",
                    "point": 2
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 1331,
                    "steamid": "[U:1:167882722]",
                    "team": "Red"
                },
                {
                    "type": "medic_death",
                    "time": 1348,
                    "team": "Red",
                    "steamid": "[U:1:167882722]",
                    "killer": "[U:1:125148025]"
                },
                {
                    "type": "pointcap",
                    "time": 1387,
                    "team": "Blue",
                    "point": 2
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 1389,
                    "steamid": "[U:1:88031169]",
                    "team": "Blue"
                },
                {
                    "type": "medic_death",
                    "time": 1400,
                    "team": "Red",
                    "steamid": "[U:1:167882722]",
                    "killer": "[U:1:125148025]"
                },
                {
                    "type": "medic_death",
                    "time": 1410,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:119246276]"
                },
                {
                    "type": "pointcap",
                    "time": 1415,
                    "team": "Blue",
                    "point": 3
                },
                {
                    "type": "pointcap",
                    "time": 1442,
                    "team": "Blue",
                    "point": 4
                },
                {
                    "type": "pointcap",
                    "time": 1464,
                    "team": "Blue",
                    "point": 5
                },
                {
                    "type": "round_win",
                    "time": 1464,
                    "team": "Blue"
                }
            ],
            "players": {
                "[U:1:125148025]": {
                    "team": "Blue",
                    "kills": 3,
                    "dmg": 1235
                },
                "[U:1:355240130]": {
                    "team": "Blue",
                    "kills": 8,
                    "dmg": 1899
                },
                "[U:1:96727704]": {
                    "team": "Red",
                    "kills": 3,
                    "dmg": 1305
                },
                "[U:1:102992936]": {
                    "team": "Blue",
                    "kills": 5,
                    "dmg": 2270
                },
                "[U:1:162288532]": {
                    "team": "Blue",
                    "kills": 5,
                    "dmg": 1531
                },
                "[U:1:108763985]": {
                    "team": "Red",
                    "kills": 6,
                    "dmg": 2852
                },
                "[U:1:321959931]": {
                    "team": "Red",
                    "kills": 3,
                    "dmg": 919
                },
                "[U:1:167882722]": {
                    "team": "Red",
                    "kills": 0,
                    "dmg": 107
                },
                "[U:1:102670289]": {
                    "team": "Blue",
                    "kills": 4,
                    "dmg": 1765
                },
                "[U:1:84854265]": {
                    "team": "Red",
                    "kills": 3,
                    "dmg": 2070
                },
                "[U:1:119246276]": {
                    "team": "Red",
                    "kills": 4,
                    "dmg": 1344
                },
                "[U:1:88031169]": {
                    "team": "Blue",
                    "kills": 1,
                    "dmg": 83
                },
                "[U:1:87283349]": {
                    "team": None,
                    "kills": 0,
                    "dmg": 0
                }
            },
            "firstcap": "Red",
            "length": 355
        },
        {
            "start_time": 1507319695,
            "winner": "Blue",
            "team": {
                "Blue": {
                    "score": 3,
                    "kills": 18,
                    "dmg": 4926,
                    "ubers": 2
                },
                "Red": {
                    "score": 3,
                    "kills": 14,
                    "dmg": 4871,
                    "ubers": 0
                }
            },
            "events": [
                {
                    "type": "pointcap",
                    "time": 1528,
                    "team": "Blue",
                    "point": 3
                },
                {
                    "type": "pointcap",
                    "time": 1590,
                    "team": "Blue",
                    "point": 4
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 1592,
                    "steamid": "[U:1:88031169]",
                    "team": "Blue"
                },
                {
                    "type": "drop",
                    "time": 1596,
                    "team": "Red",
                    "steamid": "[U:1:167882722]"
                },
                {
                    "type": "medic_death",
                    "time": 1596,
                    "team": "Red",
                    "steamid": "[U:1:167882722]",
                    "killer": "[U:1:162288532]"
                },
                {
                    "type": "medic_death",
                    "time": 1671,
                    "team": "Red",
                    "steamid": "[U:1:167882722]",
                    "killer": "[U:1:102670289]"
                },
                {
                    "type": "charge",
                    "medigun": "medigun",
                    "time": 1674,
                    "steamid": "[U:1:88031169]",
                    "team": "Blue"
                },
                {
                    "type": "pointcap",
                    "time": 1679,
                    "team": "Blue",
                    "point": 5
                },
                {
                    "type": "round_win",
                    "time": 1679,
                    "team": "Blue"
                }
            ],
            "players": {
                "[U:1:96727704]": {
                    "team": "Red",
                    "kills": 6,
                    "dmg": 1129
                },
                "[U:1:162288532]": {
                    "team": "Blue",
                    "kills": 3,
                    "dmg": 1455
                },
                "[U:1:125148025]": {
                    "team": "Blue",
                    "kills": 4,
                    "dmg": 756
                },
                "[U:1:321959931]": {
                    "team": "Red",
                    "kills": 1,
                    "dmg": 419
                },
                "[U:1:84854265]": {
                    "team": "Red",
                    "kills": 4,
                    "dmg": 1872
                },
                "[U:1:355240130]": {
                    "team": "Blue",
                    "kills": 4,
                    "dmg": 956
                },
                "[U:1:119246276]": {
                    "team": "Red",
                    "kills": 1,
                    "dmg": 678
                },
                "[U:1:102670289]": {
                    "team": "Blue",
                    "kills": 3,
                    "dmg": 893
                },
                "[U:1:102992936]": {
                    "team": "Blue",
                    "kills": 3,
                    "dmg": 736
                },
                "[U:1:167882722]": {
                    "team": "Red",
                    "kills": 0,
                    "dmg": 111
                },
                "[U:1:108763985]": {
                    "team": "Red",
                    "kills": 2,
                    "dmg": 662
                },
                "[U:1:88031169]": {
                    "team": "Blue",
                    "kills": 1,
                    "dmg": 130
                },
                "[U:1:87283349]": {
                    "team": None,
                    "kills": 0,
                    "dmg": 0
                }
            },
            "firstcap": "Blue",
            "length": 209
        },
        {
            "start_time": 1507319909,
            "winner": None,
            "team": {
                "Blue": {
                    "score": 3,
                    "kills": 5,
                    "dmg": 1930,
                    "ubers": 0
                },
                "Red": {
                    "score": 3,
                    "kills": 12,
                    "dmg": 2600,
                    "ubers": 0
                }
            },
            "events": [
                {
                    "type": "medic_death",
                    "time": 1719,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:108763985]"
                },
                {
                    "type": "medic_death",
                    "time": 1760,
                    "team": "Blue",
                    "steamid": "[U:1:88031169]",
                    "killer": "[U:1:84854265]"
                },
                {
                    "type": "pointcap",
                    "time": 1779,
                    "team": "Red",
                    "point": 3
                },
                {
                    "type": "pointcap",
                    "time": 1796,
                    "team": "Red",
                    "point": 2
                },
                {
                    "type": "round_win",
                    "time": 1799,
                    "team": None
                }
            ],
            "players": {
                "[U:1:96727704]": {
                    "team": "Red",
                    "kills": 6,
                    "dmg": 1017
                },
                "[U:1:108763985]": {
                    "team": "Red",
                    "kills": 2,
                    "dmg": 404
                },
                "[U:1:84854265]": {
                    "team": "Red",
                    "kills": 2,
                    "dmg": 725
                },
                "[U:1:162288532]": {
                    "team": "Blue",
                    "kills": 0,
                    "dmg": 186
                },
                "[U:1:102992936]": {
                    "team": "Blue",
                    "kills": 0,
                    "dmg": 496
                },
                "[U:1:355240130]": {
                    "team": "Blue",
                    "kills": 5,
                    "dmg": 565
                },
                "[U:1:102670289]": {
                    "team": "Blue",
                    "kills": 0,
                    "dmg": 430
                },
                "[U:1:321959931]": {
                    "team": "Red",
                    "kills": 1,
                    "dmg": 177
                },
                "[U:1:119246276]": {
                    "team": "Red",
                    "kills": 1,
                    "dmg": 221
                },
                "[U:1:88031169]": {
                    "team": "Blue",
                    "kills": 0,
                    "dmg": 103
                },
                "[U:1:125148025]": {
                    "team": "Blue",
                    "kills": 0,
                    "dmg": 150
                },
                "[U:1:167882722]": {
                    "team": "Red",
                    "kills": 0,
                    "dmg": 56
                },
                "[U:1:87283349]": {
                    "team": None,
                    "kills": 0,
                    "dmg": 0
                }
            },
            "firstcap": "Red",
            "length": 115
        }
    ],
    "healspread": {
        "[U:1:167882722]": {
            "[U:1:84854265]": 9356,
            "[U:1:108763985]": 4589,
            "[U:1:96727704]": 2306,
            "[U:1:321959931]": 1677,
            "[U:1:119246276]": 4777
        },
        "[U:1:88031169]": {
            "[U:1:355240130]": 3646,
            "[U:1:162288532]": 2674,
            "[U:1:125148025]": 3160,
            "[U:1:102670289]": 10204,
            "[U:1:102992936]": 6159,
            "[U:1:119246276]": 51
        }
    },
    "classkills": {
        "[U:1:321959931]": {
            "scout": 7,
            "demoman": 3,
            "medic": 1,
            "soldier": 2
        },
        "[U:1:119246276]": {
            "soldier": 6,
            "scout": 3,
            "medic": 3,
            "demoman": 6,
            "sniper": 3
        },
        "[U:1:96727704]": {
            "soldier": 9,
            "medic": 3,
            "scout": 14,
            "demoman": 3,
            "sniper": 2,
            "heavyweapons": 1,
            "engineer": 1
        },
        "[U:1:162288532]": {
            "medic": 5,
            "demoman": 3,
            "soldier": 6,
            "scout": 9
        },
        "[U:1:355240130]": {
            "scout": 13,
            "soldier": 10,
            "demoman": 5,
            "medic": 1,
            "sniper": 3,
            "spy": 2
        },
        "[U:1:84854265]": {
            "soldier": 15,
            "scout": 2,
            "medic": 2,
            "sniper": 1
        },
        "[U:1:108763985]": {
            "scout": 9,
            "soldier": 14,
            "demoman": 3,
            "medic": 5,
            "sniper": 5
        },
        "[U:1:102670289]": {
            "medic": 3,
            "soldier": 4,
            "scout": 5,
            "demoman": 3
        },
        "[U:1:102992936]": {
            "soldier": 7,
            "scout": 6,
            "heavyweapons": 1,
            "pyro": 3
        },
        "[U:1:125148025]": {
            "scout": 12,
            "demoman": 6,
            "soldier": 8,
            "medic": 3,
            "spy": 1
        },
        "[U:1:167882722]": {
            "scout": 1
        },
        "[U:1:88031169]": {
            "soldier": 1,
            "engineer": 1,
            "spy": 1
        }
    },
    "classdeaths": {
        "[U:1:102992936]": {
            "scout": 6,
            "soldier": 8,
            "medic": 1,
            "spy": 1
        },
        "[U:1:162288532]": {
            "soldier": 17,
            "demoman": 6,
            "scout": 6
        },
        "[U:1:102670289]": {
            "scout": 4,
            "demoman": 10,
            "soldier": 3,
            "pyro": 1
        },
        "[U:1:167882722]": {
            "soldier": 8,
            "demoman": 1,
            "scout": 3
        },
        "[U:1:321959931]": {
            "demoman": 9,
            "scout": 7,
            "soldier": 7,
            "sniper": 2,
            "heavyweapons": 1,
            "engineer": 1
        },
        "[U:1:84854265]": {
            "soldier": 6,
            "scout": 7,
            "demoman": 1,
            "sniper": 2,
            "heavyweapons": 1
        },
        "[U:1:88031169]": {
            "scout": 3,
            "soldier": 8,
            "sniper": 1,
            "demoman": 2
        },
        "[U:1:119246276]": {
            "demoman": 3,
            "scout": 9,
            "medic": 3,
            "soldier": 6,
            "sniper": 1,
            "engineer": 2
        },
        "[U:1:96727704]": {
            "demoman": 4,
            "scout": 11,
            "soldier": 7,
            "sniper": 1,
            "heavyweapons": 1,
            "engineer": 1
        },
        "[U:1:355240130]": {
            "scout": 12,
            "soldier": 10,
            "engineer": 1,
            "pyro": 1
        },
        "[U:1:125148025]": {
            "soldier": 9,
            "scout": 12,
            "demoman": 2
        },
        "[U:1:108763985]": {
            "scout": 6,
            "soldier": 4,
            "demoman": 5,
            "heavyweapons": 1,
            "engineer": 1
        }
    },
    "classkillassists": {
        "[U:1:321959931]": {
            "scout": 7,
            "demoman": 3,
            "medic": 1,
            "soldier": 8
        },
        "[U:1:119246276]": {
            "soldier": 11,
            "scout": 6,
            "medic": 4,
            "demoman": 7,
            "sniper": 3
        },
        "[U:1:108763985]": {
            "soldier": 19,
            "scout": 14,
            "demoman": 3,
            "medic": 5,
            "sniper": 5,
            "heavyweapons": 1
        },
        "[U:1:96727704]": {
            "soldier": 11,
            "scout": 17,
            "medic": 3,
            "demoman": 5,
            "sniper": 3,
            "heavyweapons": 1,
            "engineer": 1
        },
        "[U:1:162288532]": {
            "medic": 5,
            "scout": 18,
            "demoman": 4,
            "soldier": 9,
            "pyro": 1
        },
        "[U:1:355240130]": {
            "scout": 13,
            "demoman": 7,
            "soldier": 14,
            "medic": 2,
            "sniper": 3,
            "spy": 2,
            "heavyweapons": 1,
            "pyro": 1
        },
        "[U:1:84854265]": {
            "soldier": 16,
            "scout": 4,
            "medic": 3,
            "sniper": 2
        },
        "[U:1:167882722]": {
            "soldier": 7,
            "demoman": 1,
            "scout": 2,
            "medic": 1
        },
        "[U:1:102670289]": {
            "medic": 3,
            "soldier": 8,
            "scout": 8,
            "demoman": 3,
            "sniper": 1,
            "pyro": 1
        },
        "[U:1:102992936]": {
            "soldier": 11,
            "scout": 8,
            "medic": 2,
            "engineer": 1,
            "heavyweapons": 1,
            "pyro": 3
        },
        "[U:1:125148025]": {
            "scout": 14,
            "soldier": 11,
            "demoman": 7,
            "medic": 3,
            "spy": 1
        },
        "[U:1:88031169]": {
            "soldier": 4,
            "scout": 1,
            "demoman": 1,
            "engineer": 1,
            "medic": 1,
            "spy": 1
        }
    },
    "chat": [
        {
            "steamid": "[U:1:162288532]",
            "name": "Eternal",
            "msg": "ur mean"
        },
        {
            "steamid": "[U:1:108763985]",
            "name": "emgee",
            "msg": "soz"
        },
        {
            "steamid": "[U:1:321959931]",
            "name": "LZER",
            "msg": "npoo"
        },
        {
            "steamid": "[U:1:321959931]",
            "name": "LZER",
            "msg": "shit"
        },
        {
            "steamid": "[U:1:321959931]",
            "name": "LZER",
            "msg": "lol"
        },
        {
            "steamid": "[U:1:321959931]",
            "name": "LZER",
            "msg": "dab"
        },
        {
            "steamid": "[U:1:125148025]",
            "name": "chezs",
            "msg": ":("
        },
        {
            "steamid": "[U:1:125148025]",
            "name": "chezs",
            "msg": ":(((("
        },
        {
            "steamid": "[U:1:108763985]",
            "name": "emgee",
            "msg": "rip"
        },
        {
            "steamid": "[U:1:162288532]",
            "name": "Eternal",
            "msg": "u saw nothing"
        },
        {
            "steamid": "[U:1:355240130]",
            "name": "jjjjaaack",
            "msg": "noobed"
        },
        {
            "steamid": "[U:1:162288532]",
            "name": "Eternal",
            "msg": "how do hit laggy medic"
        },
        {
            "steamid": "[U:1:108763985]",
            "name": "emgee",
            "msg": "tfw no escape plan :("
        },
        {
            "steamid": "[U:1:321959931]",
            "name": "LZER",
            "msg": ":)"
        },
        {
            "steamid": "[U:1:321959931]",
            "name": "LZER",
            "msg": "anyone wanna play roblox after?"
        },
        {
            "steamid": "[U:1:162288532]",
            "name": "Eternal",
            "msg": "no"
        },
        {
            "steamid": "[U:1:162288532]",
            "name": "Eternal",
            "msg": "my window"
        },
        {
            "steamid": "[U:1:119246276]",
            "name": "my nama swag",
            "msg": "8:50 PM - jjjjaaack: get off engi"
        },
        {
            "steamid": "[U:1:355240130]",
            "name": "jjjjaaack",
            "msg": "parking the bus"
        },
        {
            "steamid": "[U:1:119246276]",
            "name": "my nama swag",
            "msg": "8:50 PM - jjjjaaack: get off engi"
        },
        {
            "steamid": "[U:1:119246276]",
            "name": "my nama swag",
            "msg": "8:50 PM - jjjjaaack: get off engi"
        },
        {
            "steamid": "[U:1:119246276]",
            "name": "my nama swag",
            "msg": "8:50 PM - jjjjaaack: get off engi"
        },
        {
            "steamid": "[U:1:119246276]",
            "name": "my nama swag",
            "msg": "8:50 PM - jjjjaaack: get off engi"
        },
        {
            "steamid": "[U:1:321959931]",
            "name": "LZER",
            "msg": "lol"
        },
        {
            "steamid": "[U:1:119246276]",
            "name": "my nama swag",
            "msg": "8:50 PM - jjjjaaack: get off engi"
        },
        {
            "steamid": "[U:1:88031169]",
            "name": "jsabb",
            "msg": "GG"
        }
    ],
    "info": {
        "map": "",
        "supplemental": True,
        "total_length": 1768,
        "hasRealDamage": True,
        "hasWeaponDamage": True,
        "hasAccuracy": True,
        "hasHP": True,
        "hasHP_real": True,
        "hasHS": True,
        "hasHS_hit": True,
        "hasBS": True,
        "hasCP": True,
        "hasSB": False,
        "hasDT": True,
        "hasAS": True,
        "hasHR": True,
        "hasIntel": False,
        "AD_scoring": False,
        "notifications": []
    },
    "killstreaks": [
        {
            "steamid": "[U:1:96727704]",
            "streak": 3,
            "time": 199
        },
        {
            "steamid": "[U:1:355240130]",
            "streak": 4,
            "time": 340
        },
        {
            "steamid": "[U:1:162288532]",
            "streak": 3,
            "time": 452
        },
        {
            "steamid": "[U:1:125148025]",
            "streak": 4,
            "time": 557
        },
        {
            "steamid": "[U:1:108763985]",
            "streak": 3,
            "time": 618
        },
        {
            "steamid": "[U:1:108763985]",
            "streak": 3,
            "time": 805
        },
        {
            "steamid": "[U:1:355240130]",
            "streak": 3,
            "time": 1720
        }
    ]
}
