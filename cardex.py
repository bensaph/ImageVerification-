from urllib.request import *
from json import *
import time

def get_json(url):
    ''' Function to get a json dictionary from a website.
        url - a string'''
    with urlopen(url) as response:
        html = response.read()
    print('Loading' + '.' + '.')
    htmlstr = html.decode("utf-8")
    return loads(htmlstr)

def main():

    start = time.time()
    label_list = {
  "labelAnnotations": [
    {
      "mid": "/m/01prls",
      "description": "Land vehicle",
      "score": 0.9961627,
      "topicality": 0.9961627
    },
    {
      "mid": "/m/07yv9",
      "description": "Vehicle",
      "score": 0.99030316,
      "topicality": 0.99030316
    },
    {
      "mid": "/m/0k4j",
      "description": "Car",
      "score": 0.98701257,
      "topicality": 0.98701257
    },
    {
      "mid": "/m/03kr0",
      "description": "Honda",
      "score": 0.95472264,
      "topicality": 0.95472264
    },
    {
      "mid": "/m/025wph",
      "description": "Honda fit",
      "score": 0.91333896,
      "topicality": 0.91333896
    },
    {
      "mid": "/m/03txxp",
      "description": "Subcompact car",
      "score": 0.7992235,
      "topicality": 0.7992235
    },
    {
      "mid": "/m/01cmcs",
      "description": "Hatchback",
      "score": 0.79471,
      "topicality": 0.79471
    },
    {
      "mid": "/m/068mqj",
      "description": "Automotive design",
      "score": 0.72283965,
      "topicality": 0.72283965
    },
    {
      "mid": "/m/02swz_",
      "description": "Compact car",
      "score": 0.72116303,
      "topicality": 0.72116303
    },
    {
      "mid": "/m/0369ss",
      "description": "City car",
      "score": 0.6680848,
      "topicality": 0.6680848
    },
    {
      "mid": "/m/088l6h",
      "description": "Family car",
      "score": 0.5739651,
      "topicality": 0.5739651
    }
  ],
  "textAnnotations": [
    {
      "locale": "en",
      "description": "EVDX IMAGES\n",
      "boundingPoly": {
        "vertices": [
          {
            "x": 564,
            "y": 460
          },
          {
            "x": 627,
            "y": 460
          },
          {
            "x": 627,
            "y": 473
          },
          {
            "x": 564,
            "y": 473
          }
        ]
      }
    },
    {
      "description": "EVDX",
      "boundingPoly": {
        "vertices": [
          {
            "x": 564,
            "y": 460
          },
          {
            "x": 585,
            "y": 460
          },
          {
            "x": 585,
            "y": 473
          },
          {
            "x": 564,
            "y": 473
          }
        ]
      }
    },
    {
      "description": "IMAGES",
      "boundingPoly": {
        "vertices": [
          {
            "x": 591,
            "y": 460
          },
          {
            "x": 627,
            "y": 460
          },
          {
            "x": 627,
            "y": 473
          },
          {
            "x": 591,
            "y": 473
          }
        ]
      }
    }
  ],
  "safeSearchAnnotation": {
    "adult": "VERY_UNLIKELY",
    "spoof": "VERY_UNLIKELY",
    "medical": "VERY_UNLIKELY",
    "violence": "VERY_UNLIKELY",
    "racy": "VERY_UNLIKELY"
  },
  "imagePropertiesAnnotation": {
    "dominantColors": {
      "colors": [
        {
          "color": {
            "red": 230,
            "green": 229,
            "blue": 227
          },
          "score": 0.29008085,
          "pixelFraction": 0.77726597
        },
        {
          "color": {
            "red": 22,
            "green": 21,
            "blue": 20
          },
          "score": 0.097912006,
          "pixelFraction": 0.03947275
        },
        {
          "color": {
            "red": 81,
            "green": 81,
            "blue": 80
          },
          "score": 0.09665545,
          "pixelFraction": 0.030756148
        },
        {
          "color": {
            "red": 200,
            "green": 199,
            "blue": 197
          },
          "score": 0.25640738,
          "pixelFraction": 0.07306357
        },
        {
          "color": {
            "red": 158,
            "green": 157,
            "blue": 156
          },
          "score": 0.097829275,
          "pixelFraction": 0.029126214
        },
        {
          "color": {
            "red": 53,
            "green": 53,
            "blue": 52
          },
          "score": 0.0870516,
          "pixelFraction": 0.027212813
        },
        {
          "color": {
            "red": 121,
            "green": 121,
            "blue": 120
          },
          "score": 0.07406345,
          "pixelFraction": 0.023102544
        }
      ]
    }
  },
  "cropHintsAnnotation": {
    "cropHints": [
      {
        "boundingPoly": {
          "vertices": [
            {
              "x": 114
            },
            {
              "x": 504
            },
            {
              "x": 504,
              "y": 479
            },
            {
              "x": 114,
              "y": 479
            }
          ]
        },
        "confidence": 0.79999995,
        "importanceFraction": 0.84999996
      },
      {
        "boundingPoly": {
          "vertices": [
            {
              "x": 50
            },
            {
              "x": 536
            },
            {
              "x": 536,
              "y": 479
            },
            {
              "x": 50,
              "y": 479
            }
          ]
        },
        "confidence": 0.79999995,
        "importanceFraction": 0.97999996
      },
      {
        "boundingPoly": {
          "vertices": [
            {
              "x": 5
            },
            {
              "x": 587
            },
            {
              "x": 587,
              "y": 479
            },
            {
              "x": 5,
              "y": 479
            }
          ]
        },
        "confidence": 0.79999995,
        "importanceFraction": 0.98999995
      }
    ]
  },
  "fullTextAnnotation": {
    "pages": [
      {
        "property": {
          "detectedLanguages": [
            {
              "languageCode": "en",
              "confidence": 1
            }
          ]
        },
        "width": 640,
        "height": 480,
        "blocks": [
          {
            "boundingBox": {
              "vertices": [
                {
                  "x": 564,
                  "y": 460
                },
                {
                  "x": 627,
                  "y": 460
                },
                {
                  "x": 627,
                  "y": 473
                },
                {
                  "x": 564,
                  "y": 473
                }
              ]
            },
            "paragraphs": [
              {
                "boundingBox": {
                  "vertices": [
                    {
                      "x": 564,
                      "y": 460
                    },
                    {
                      "x": 627,
                      "y": 460
                    },
                    {
                      "x": 627,
                      "y": 473
                    },
                    {
                      "x": 564,
                      "y": 473
                    }
                  ]
                },
                "words": [
                  {
                    "property": {
                      "detectedLanguages": [
                        {
                          "languageCode": "en"
                        }
                      ]
                    },
                    "boundingBox": {
                      "vertices": [
                        {
                          "x": 564,
                          "y": 460
                        },
                        {
                          "x": 585,
                          "y": 460
                        },
                        {
                          "x": 585,
                          "y": 473
                        },
                        {
                          "x": 564,
                          "y": 473
                        }
                      ]
                    },
                    "symbols": [
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 564,
                              "y": 460
                            },
                            {
                              "x": 567,
                              "y": 460
                            },
                            {
                              "x": 567,
                              "y": 473
                            },
                            {
                              "x": 564,
                              "y": 473
                            }
                          ]
                        },
                        "text": "E",
                        "confidence": 0.91
                      },
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 569,
                              "y": 460
                            },
                            {
                              "x": 574,
                              "y": 460
                            },
                            {
                              "x": 574,
                              "y": 473
                            },
                            {
                              "x": 569,
                              "y": 473
                            }
                          ]
                        },
                        "text": "V",
                        "confidence": 0.91
                      },
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 576,
                              "y": 460
                            },
                            {
                              "x": 581,
                              "y": 460
                            },
                            {
                              "x": 581,
                              "y": 473
                            },
                            {
                              "x": 576,
                              "y": 473
                            }
                          ]
                        },
                        "text": "D",
                        "confidence": 0.8
                      },
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ],
                          "detectedBreak": {
                            "type": "SPACE"
                          }
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 582,
                              "y": 460
                            },
                            {
                              "x": 585,
                              "y": 460
                            },
                            {
                              "x": 585,
                              "y": 473
                            },
                            {
                              "x": 582,
                              "y": 473
                            }
                          ]
                        },
                        "text": "X",
                        "confidence": 0.74
                      }
                    ],
                    "confidence": 0.84
                  },
                  {
                    "property": {
                      "detectedLanguages": [
                        {
                          "languageCode": "en"
                        }
                      ]
                    },
                    "boundingBox": {
                      "vertices": [
                        {
                          "x": 591,
                          "y": 460
                        },
                        {
                          "x": 627,
                          "y": 460
                        },
                        {
                          "x": 627,
                          "y": 473
                        },
                        {
                          "x": 591,
                          "y": 473
                        }
                      ]
                    },
                    "symbols": [
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 591,
                              "y": 460
                            },
                            {
                              "x": 593,
                              "y": 460
                            },
                            {
                              "x": 593,
                              "y": 473
                            },
                            {
                              "x": 591,
                              "y": 473
                            }
                          ]
                        },
                        "text": "I",
                        "confidence": 0.9
                      },
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 593,
                              "y": 460
                            },
                            {
                              "x": 597,
                              "y": 460
                            },
                            {
                              "x": 597,
                              "y": 473
                            },
                            {
                              "x": 593,
                              "y": 473
                            }
                          ]
                        },
                        "text": "M",
                        "confidence": 0.9
                      },
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 602,
                              "y": 460
                            },
                            {
                              "x": 607,
                              "y": 460
                            },
                            {
                              "x": 607,
                              "y": 473
                            },
                            {
                              "x": 602,
                              "y": 473
                            }
                          ]
                        },
                        "text": "A",
                        "confidence": 0.98
                      },
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 607,
                              "y": 460
                            },
                            {
                              "x": 613,
                              "y": 460
                            },
                            {
                              "x": 613,
                              "y": 473
                            },
                            {
                              "x": 607,
                              "y": 473
                            }
                          ]
                        },
                        "text": "G",
                        "confidence": 1
                      },
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 617,
                              "y": 460
                            },
                            {
                              "x": 623,
                              "y": 460
                            },
                            {
                              "x": 623,
                              "y": 473
                            },
                            {
                              "x": 617,
                              "y": 473
                            }
                          ]
                        },
                        "text": "E",
                        "confidence": 0.98
                      },
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ],
                          "detectedBreak": {
                            "type": "LINE_BREAK"
                          }
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 624,
                              "y": 460
                            },
                            {
                              "x": 627,
                              "y": 460
                            },
                            {
                              "x": 627,
                              "y": 473
                            },
                            {
                              "x": 624,
                              "y": 473
                            }
                          ]
                        },
                        "text": "S",
                        "confidence": 0.99
                      }
                    ],
                    "confidence": 0.95
                  }
                ],
                "confidence": 0.91
              }
            ],
            "blockType": "TEXT",
            "confidence": 0.91
          }
        ]
      }
    ],
    "text": "EVDX IMAGES\n"
  },
  "webDetection": {
    "webEntities": [
      {
        "entityId": "/m/02k_kxs",
        "score": 1.06125,
        "description": "Honda"
      },
      {
        "entityId": "/m/03kr0",
        "score": 0.9303,
        "description": "Honda Motor Company"
      },
      {
        "entityId": "/g/11h9rc62d9",
        "score": 0.833448,
        "description": "2018 Honda Fit LX"
      },
      {
        "entityId": "/g/11gdly7ddw",
        "score": 0.710149,
        "description": "2018 Honda Fit Sport"
      },
      {
        "entityId": "/m/0y4l_bh",
        "score": 0.7075
      },
      {
        "entityId": "/m/0k4j",
        "score": 0.69315,
        "description": "Car"
      },
      {
        "entityId": "/g/11f5tbygtz",
        "score": 0.668767,
        "description": "2019 Honda Fit LX"
      },
      {
        "entityId": "/g/11b5wf0s2p",
        "score": 0.5882,
        "description": "LeDé Sports"
      },
      {
        "entityId": "/g/1tjyn9p6",
        "score": 0.5361,
        "description": "Miramichi Honda"
      },
      {
        "entityId": "/g/11c3kcbq04",
        "score": 0.4978,
        "description": "lx"
      },
      {
        "entityId": "/m/07n7lk",
        "score": 0.4901,
        "description": "Car dealership"
      },
      {
        "entityId": "/g/1t_tjxcv",
        "score": 0.4372,
        "description": "Honda de La Capitale"
      },
      {
        "entityId": "/g/11g079kf2l",
        "score": 0.18001172,
        "description": "2019 Honda Fit"
      },
      {
        "entityId": "/g/11gdlxnl23",
        "score": 0.046057444,
        "description": "2018 Honda Fit"
      },
      {
        "entityId": "/m/025wph",
        "score": 0.000013553282,
        "description": "Honda Fit"
      }
    ],
    "fullMatchingImages": [
      {
        "url": "http://img.sm360.ca/ir/w710h534/images/newcar/ca/2019/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
      },
      {
        "url": "http://img1.sm360.ca/images/newcar/2018/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
      },
      {
        "url": "https://img.sm360.ca/images/newcar/ca/2019/honda/fit/lx-sensing/hatchback/exteriorColors/12182_cc0640_032_wa.png"
      },
      {
        "url": "http://img0.sm360.ca/images/newcar/ca/2019/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
      },
      {
        "url": "http://cdn-ds.com/evox/2019-Honda-FIT-LX-HS-St-Johns-NL/seo/color_0640_032/12816/w_640/h_480/12816_cc0640_032_WA.jpg"
      },
      {
        "url": "http://file.kelleybluebookimages.com/kbb/vehicleimage/evoxseo/cp/l/8951/2014-toyota-yaris-front_8951_032_640x480_040.png"
      },
      {
        "url": "http://img1.sm360.ca/images/newcar/2018/buick/envision/preferred/suv/exteriorColors/12446_cc0640_032_GAZ.png"
      },
      {
        "url": "https://inventory-cf.assets-cdk.com/evox/color_0640_032_png/12446/12446_cc0640_032_GAZ.png"
      },
      {
        "url": "http://img0.sm360.ca/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
      },
      {
        "url": "https://inventory-cf.assets-cdk.com/evox/color_0640_032_png/12182/12182_cc0640_032_WA.png"
      },
      {
        "url": "http://schedulebull.com/?img=rjIyCJ5slQ9qWRAhsA~e~e"
      },
      {
        "url": "http://bestcarmag.com/sites/default/files/2016-ford-c-max-energi-1880479-7165205.png"
      },
      {
        "url": "https://img1.sm360.ca/ir/w940/images/newcar/2018/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
      },
      {
        "url": "https://inventory-cf.assets-cdk.com/evox/color_0640_032/4863/4863_cc0640_032_UD.jpg"
      },
      {
        "url": "https://img.sm360.ca/ir/w600h450/images/newcar/2018/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
      },
      {
        "url": "http://img0.sm360.ca/ir/w600h450/images/newcar/ca/2019/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
      },
      {
        "url": "http://img0.sm360.ca/ir/w580h435c/images/newcar/ca/2019/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
      },
      {
        "url": "http://img2.sm360.ca/ir/w580h435c/images/newcar/ca/2019/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
      },
      {
        "url": "https://img.sm360.ca/ir/w450h450/images/newcar/ca/2019/honda/fit/lx-sensing/hatchback/exteriorColors/12182_cc0640_032_wa.png"
      },
      {
        "url": "https://carfax-img.vast.com/carfax/-3702774292573796331/1/344x258"
      },
      {
        "url": "https://pictures.dealer.com/a/apostolakishonda/0260/aa6bdbe602166a311a89bac3d3b59558x.jpg?impolicy=resize&amp;w=320"
      },
      {
        "url": "https://img.sm360.ca/ir/w294h233c/images/newcar/ca/2019/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
      },
      {
        "url": "https://pictures.dealer.com/a/apostolakishonda/0260/aa6bdbe602166a311a89bac3d3b59558x.jpg?impolicy=resize&amp;w=240"
      },
      {
        "url": "https://pictures.dealer.com/b/boydchevyemporia/1287/ddb87c0a8d13c232a6ad2568721c2d28x.jpg?impolicy=resize&amp;w=240"
      },
      {
        "url": "https://cdn.vehiclemall.com/evox/8935/8935_cc0640_032_040.png?scale=both&amp;maxwidth=190&amp;quality=80"
      }
    ],
    "partialMatchingImages": [
      {
        "url": "https://png2.kisspng.com/20180907/klk/kisspng-honda-motor-company-car-2-16-honda-fit-2-19-honda-go-to-image-page-5b929c5c105464.3737869115363349400669.png"
      },
      {
        "url": "https://img2.carmax.com/stock/mm-Honda-Fit/1200"
      },
      {
        "url": "https://img2.carmax.com/stock/mmy-Honda-Fit-2013/1200"
      },
      {
        "url": "https://http2.mlstatic.com/par-moldura-led-daylight-luz-diurna-honda-fit-2018-s-milha-D_NQ_NP_939942-MLB27798153274_072018-F.jpg"
      },
      {
        "url": "https://images-na.ssl-images-amazon.com/images/I/61q5NZZMJ1L._SL1200_.jpg"
      },
      {
        "url": "https://globalsewamobilpekanbaru.com/wp-content/uploads/2018/12/JAZZ.jpg"
      },
      {
        "url": "https://static.tcimg.net/vehicles/primary/7efcf1db78a008cf/2019-Honda-Fit-white-full_color-driver_side_front_quarter.png"
      },
      {
        "url": "http://www.edmundmotor.com.sg/wp-content/uploads/2018/11/Honda-Fit-1024x640.png"
      },
      {
        "url": "https://ae01.alicdn.com/kf/HTB1BPMrKeySBuNjy1zdq6xPxFXaU.jpg"
      },
      {
        "url": "https://www.honda.co.jp/Fit/webcatalog/type/gasoline/image/gs_f/pic_gs_f_platinum_white_sp.jpg"
      },
      {
        "url": "https://banner2.kisspng.com/20180907/hvb/kisspng-honda-motor-company-car-2-16-honda-fit-2-19-honda-go-to-image-page-5b929c5bcc8f24.5800890615363349398379.jpg"
      },
      {
        "url": "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=10156937780323958"
      },
      {
        "url": "https://banner2.kisspng.com/20180710/wgk/kisspng-2019-honda-fit-car-hyundai-2017-honda-fit-ex-l-honda-hrv-2018-5b4515ecd88d12.222665921531254252887.jpg"
      },
      {
        "url": "https://scontent-lga3-1.cdninstagram.com/vp/2c921ab8c8b17f2c2165b0cd38c69591/5C48EA64/t51.2885-15/sh0.08/e35/c0.135.1080.1080/s640x640/40030488_2107790896149463_885692672424017920_n.jpg"
      },
      {
        "url": "https://t4.aimg.sk/inzercie/ab_orig_82376654_bmw-rad-2-active-tourer-bmw-rad-2-active-tourer-218d-xdrive-m-sport-f45.jpg?t=LzcyMHg1NDAvZmlsdGVyczpxdWFsaXR5KDc1KQ%3D%3D&amp;h=Kw-nNeIqsdHVoWDVWupxEg&amp;e=2145916800"
      },
      {
        "url": "https://img.sm360.ca/ir/w770h435c/images/newcar/ca/2019/honda/fit/ex/hatchback/exteriorColors/12149_cc0640_032_wa.png"
      },
      {
        "url": "https://img.sm360.ca/ir/w770h435c/images/newcar/2018/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
      },
      {
        "url": "http://img0.sm360.ca/ir/w770h435c/images/newcar/ca/2019/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
      },
      {
        "url": "http://img0.sm360.ca/ir/w770h435c/images/newcar/ca/2019/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
      },
      {
        "url": "http://img2.sm360.ca/ir/w770h435c/images/newcar/ca/2019/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
      },
      {
        "url": "http://kuruma-kamisama.com/wp-content/uploads/2018/09/2018-10-06-1.png"
      },
      {
        "url": "https://pictures.dealer.com/t/terryleehondaofavon/0814/0105c6aa6c7259122dc0afbe1aa6ab97x.jpg?impolicy=resize&amp;w=650"
      },
      {
        "url": "https://inventory-cf.assets-cdk.com/evox/color_0640_032_png/12816/12816_cc0640_032_YE.png"
      },
      {
        "url": "https://file.kbb.com/kbb/base/evox/cp/12182/2019-honda-fit-front_12182_032_2400x1800_wb.png?interpolation=high-quality&amp;downsize=640:*"
      },
      {
        "url": "https://inventory-cf.assets-cdk.com/9/8/4/18511529489.jpg"
      },
      {
        "url": "https://cdn-ds.com/evox/2014-Kia-Forte-LX-Akron-OH/seo/color_0640_032/8847/w_640/h_480/8847_cc0640_032_SWP.jpg"
      },
      {
        "url": "http://mustafamahmoud.site/wp-content/uploads/2018/04/honda-fit-2018-colors-fit-ex-hatchback-best-new-cars-for-30000.jpg"
      },
      {
        "url": "http://www.lcdpvillaallende.com.ar/pub/media/catalog/product/cache/image/1000x1320/e9c3970ab036de70892d86c6d221abfe/2/0/2016_honda_fit_front.png"
      },
      {
        "url": "https://cdn.getauto.com/photos/4/226794/1c/19XFB4F36EE001326-1c.jpg"
      },
      {
        "url": "https://static.tcimg.net/vehicles/primary/54eca0803b698436/2019-Honda-Fit-white-full_color-driver_side_front_quarter.png"
      },
      {
        "url": "https://cdn.getauto.com/photos/0/1860/1c/3HGGK5H88KM710684-1c.jpg?201812211720"
      },
      {
        "url": "http://cdn-ds.com/stock/2019-Chevrolet-Cruze-LT-Washington-DC/seo/DS3460-1G1BE5SM7K7133803/sz_55096/1G1BE5SM7K7133803-1c.jpg"
      },
      {
        "url": "https://img.sm360.ca/images/newcar/ca/2019/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
      },
      {
        "url": "https://cdn.getauto.com/photos/6/228766/1c/3HGGK5H43KM712064-1c.jpg?201901011825"
      },
      {
        "url": "https://inventory-cf.assets-cdk.com/6/0/3/18397366306.jpg"
      },
      {
        "url": "https://file.kbb.com/kbb/vehicleimage/evoxseo/cp/l/12182/2018-honda-fit-front_12182_032_640x480_wb.png"
      },
      {
        "url": "http://cdn-ds.com/stock/2019-Honda-Fit-LX-Vineland-NJ/seo/DS21575-3HGGK5H41KM715190/sz_73017/3HGGK5H41KM715190-1c.jpg"
      },
      {
        "url": "https://img.sm360.ca/images/newcar/ca/2019/honda/fit/sport-sensing/hatchback/exteriorColors/12149_cc0640_032_wa.png"
      },
      {
        "url": "http://img.sm360.ca/images/newcar/ca/2019/honda/fit/sport-sensing/hatchback/exteriorColors/12149_cc0640_032_wa.png"
      },
      {
        "url": "http://img.sm360.ca/ir/w710h534/images/newcar/ca/2019/honda/fit/sport-sensing/hatchback/exteriorColors/12149_cc0640_032_wa.png"
      },
      {
        "url": "https://inventory-cf.assets-cdk.com/7/9/3/18558912397.jpg"
      },
      {
        "url": "https://i.ebayimg.com/00/s/NDgwWDY0MA==/z/LhcAAOSwYuNbUFsU/$_20.JPG?set_id=2"
      },
      {
        "url": "https://file.kbb.com/kbb/vehicleimage/evoxseo/cp/l/12183/2018-honda-fit-front_12183_032_640x480_wb.png"
      },
      {
        "url": "http://mustafamahmoud.site/wp-content/uploads/2017/12/2018-honda-fit-yellow-fit-vehicle-photo-in-pa-10-best-new-cars-under-30000.jpg"
      },
      {
        "url": "http://cdn-ds.com/evox/2019-Honda-FIT-SPORT-HS-St-Johns-NL/seo/color_0640_032/12817/w_640/h_480/12817_cc0640_032_WA.jpg"
      },
      {
        "url": "https://file.kbb.com/kbb/vehicleimage/evoxseo/cp/l/11500/2017-honda-fit-front_11500_032_640x480_wa.png?interpolation=high-quality&amp;crop=1.0xw:0.90xh;left,top&amp;downsize=640:*"
      },
      {
        "url": "https://file.kbb.com/kbb/vehicleimage/evoxseo/cp/l/12182/2018-honda-fit-front_12182_032_640x480_wb.png?interpolation=high-quality&amp;crop=1.0xw:0.90xh;left,top&amp;downsize=640:*"
      },
      {
        "url": "https://images.tixuz.com/cdn2/ph/3/2018/08/22/files/3999810ph19027.jpg"
      },
      {
        "url": "https://pics.tixuz.com/pics2/ph/3/2018/12/20/files/5496071ph13301.jpg"
      },
      {
        "url": "https://images.tixuz.com/cdn2/ph/3/2018/12/19/files/5475286ph371641.jpg"
      }
    ],
    "pagesWithMatchingImages": [
      {
        "url": "https://www.mooredeals.com/models/2018-honda-fit",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; Details | Don Moore Automotive Owensboro &amp;amp; Hartford",
        "fullMatchingImages": [
          {
            "url": "https://inventory-cf.assets-cdk.com/evox/color_0640_032_png/12182/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.miramichihonda.com/en/new/details/honda/fit/2018/lx/2505/7640",
        "pageTitle": "Miramichi Honda | New &lt;b&gt;2018 Honda Fit LX&lt;/b&gt; for sale in Miramichi",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w170/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.charper.com/models/2018-honda-fit",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; - C Harper Auto Group",
        "fullMatchingImages": [
          {
            "url": "https://inventory-cf.assets-cdk.com/evox/color_0640_032_png/12182/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "http://www.ledesportshonda.ca/en/new/configurations/honda/fit/2018/lx/2505/7640",
        "pageTitle": "LeDé Sports | New &lt;b&gt;2018 Honda Fit LX&lt;/b&gt; for sale in L&amp;#39;Étang-du-Nord",
        "fullMatchingImages": [
          {
            "url": "http://img.sm360.ca/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "http://www.kingshonda.com/en/new/details/honda/fit/2018/lx/2505/7640",
        "pageTitle": "Kings County Honda | New &lt;b&gt;2018 Honda Fit LX&lt;/b&gt; for sale in Kentville",
        "fullMatchingImages": [
          {
            "url": "http://img.sm360.ca/ir/w170/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          },
          {
            "url": "http://img.sm360.ca/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "http://www.cumberlandhonda.com/en/new/details/honda/fit/2018/lx/2505/7640",
        "pageTitle": "Cumberland Honda | New &lt;b&gt;2018 Honda Fit LX&lt;/b&gt; for sale in Amherst",
        "partialMatchingImages": [
          {
            "url": "http://img.sm360.ca/ir/w170/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.ivhonda.com/models/2018-honda-fit",
        "pageTitle": "&lt;b&gt;2018 Honda Fit LX&lt;/b&gt; - Imperial Valley Honda is a El Centro Honda ...",
        "fullMatchingImages": [
          {
            "url": "https://inventory-cf.assets-cdk.com/evox/color_0640_032_png/12182/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.lallierhondahull.com/en/new/details/honda/fit/2018/lx/2505/7640",
        "pageTitle": "&lt;b&gt;2018 Honda Fit LX&lt;/b&gt; - Lallier Honda Hull in Gatineau",
        "fullMatchingImages": [
          {
            "url": "https://img0.sm360.ca/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "http://www.porthonda.ca/en/new/details/honda/fit/2018/lx/2505/7640",
        "pageTitle": "Port Honda | New &lt;b&gt;2018 Honda Fit LX&lt;/b&gt; for sale in Port Hawkesbury",
        "fullMatchingImages": [
          {
            "url": "http://img.sm360.ca/ir/w170/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          },
          {
            "url": "http://img.sm360.ca/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.billywoodhonda.com/models/2018-honda-fit",
        "pageTitle": "&lt;b&gt;2018 Honda Fit LX&lt;/b&gt; - Billy Wood Honda",
        "fullMatchingImages": [
          {
            "url": "https://inventory-cf.assets-cdk.com/evox/color_0640_032_png/12182/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.hondadelaval.com/en/new/details/honda/fit/2018/lx/2505/7640",
        "pageTitle": "&lt;b&gt;2018 Honda Fit LX&lt;/b&gt; - Honda de Laval",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w170/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "http://www.ledesportshonda.ca/en/new/configurations/honda/fit/2018/sport/2505/7636",
        "pageTitle": "LeDé Sports | New &lt;b&gt;2018 Honda Fit&lt;/b&gt; SPORT for sale in L&amp;#39;Étang-du-Nord",
        "partialMatchingImages": [
          {
            "url": "http://img.sm360.ca/images/newcar/2018/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "https://www.phillong.com/models/2018-honda-fit",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; - Phil Long Dealerships",
        "fullMatchingImages": [
          {
            "url": "https://inventory-cf.assets-cdk.com/evox/color_0640_032_png/12182/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "http://www.hondadelacapitale.com/en/new/details/honda/fit/2018/lx/2505/7640",
        "pageTitle": "Honda de la Capitale | New &lt;b&gt;2018 Honda Fit LX&lt;/b&gt; for sale in Val-Bélair",
        "partialMatchingImages": [
          {
            "url": "http://img.sm360.ca/ir/w170/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.chagnonhonda.com/en/new-catalog/honda/2018-honda-fit-lx-id7640",
        "pageTitle": "Chagnon Honda | New &lt;b&gt;2018 Honda Fit LX&lt;/b&gt; for sale in Granby",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w170/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.miramichihonda.com/en/new/details/honda/fit/2019/lx/3034/9607",
        "pageTitle": "Miramichi &lt;b&gt;Honda&lt;/b&gt; | New 2019 &lt;b&gt;Honda Fit LX&lt;/b&gt; for sale in Miramichi",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w170/images/newcar/ca/2019/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "http://www.spinellihonda.com/en/new-catalog/honda/2018-honda-fit-dx-id7637",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; for sale in Montreal (near Laval) | Spinelli Honda",
        "fullMatchingImages": [
          {
            "url": "http://img2.sm360.ca/ir/w220h165c/images/newcar/ca/2019/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
          },
          {
            "url": "http://img1.sm360.ca/images/newcar/2018/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.deragonmontreal.com/en/new/details/honda/fit/2018/lx/2505/7640",
        "pageTitle": "Deragon Montreal | New &lt;b&gt;2018 Honda Fit LX&lt;/b&gt; for sale in Montreal",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w170/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.sheehy.com/models/2018-honda-fit",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; - Sheehy Auto Stores",
        "fullMatchingImages": [
          {
            "url": "https://inventory-cf.assets-cdk.com/evox/color_0640_032_png/12182/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.hillsidehonda.com/new-vehicles/fit/",
        "pageTitle": "New &lt;b&gt;Honda Fit&lt;/b&gt; in Jamaica | Hillside &lt;b&gt;Honda&lt;/b&gt;",
        "partialMatchingImages": [
          {
            "url": "https://be7bfe9e3b2884d03f3f-0605913de76b64cce9fc1256f2da7a26.ssl.cf1.rackcdn.com//thumbnails/3HGGK5H84KM710438/f8b3366cd6ada2c3064317ed2fa7a66b.jpg"
          }
        ]
      },
      {
        "url": "http://www.ledesportshonda.ca/en/new/configurations/honda/fit/2019/lx/3034/9607",
        "pageTitle": "LeDé Sports | New 2019 &lt;b&gt;Honda Fit LX&lt;/b&gt; for sale in L&amp;#39;Étang-du-Nord",
        "fullMatchingImages": [
          {
            "url": "http://img.sm360.ca/images/newcar/ca/2019/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "https://www.civicmotors.com/en/new/details/honda/fit/2018/sport/2505/7636",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; SPORT - Civic Motors Honda in Ottawa",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w500c/images/newcar/2018/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          },
          {
            "url": "https://img.sm360.ca/images/newcar/2018/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "https://www.edmunds.com/used-honda-fit-indianapolis-in/",
        "pageTitle": "Used &lt;b&gt;Honda Fit&lt;/b&gt; for Sale in Indianapolis, IN | Edmunds",
        "partialMatchingImages": [
          {
            "url": "https://media.ed.edmunds-media.com/for-sale/bc-jhmgk5h55gx003823/img-1-400x175.jpg"
          }
        ]
      },
      {
        "url": "http://www.ramsayshonda.com/en/new/details/honda/fit/2018/lx/2505/7640",
        "pageTitle": "Ramsays Honda | New &lt;b&gt;2018 Honda Fit LX&lt;/b&gt; for sale in Sydney",
        "partialMatchingImages": [
          {
            "url": "http://img.sm360.ca/ir/w170/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.miramichihonda.com/en/new/details/honda/fit/2018/sport/2505/7636",
        "pageTitle": "Miramichi Honda | New &lt;b&gt;2018 Honda Fit&lt;/b&gt; SPORT for sale in Miramichi",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w500c/images/newcar/2018/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "http://www.edmundstonhonda.com/en/new/details/honda/fit/2018/lx/2505/7640",
        "pageTitle": "New &lt;b&gt;2018 Honda Fit LX&lt;/b&gt; | Edmundston Honda",
        "fullMatchingImages": [
          {
            "url": "http://img0.sm360.ca/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.lallierhondamontreal.com/en/new-catalog/honda/2018-honda-fit-lx-id7640",
        "pageTitle": "&lt;b&gt;2018 Honda Fit LX&lt;/b&gt; - Lallier Honda Montreal in Montréal",
        "fullMatchingImages": [
          {
            "url": "https://img0.sm360.ca/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.truecar.com/prices-new/honda/fit-pricing/",
        "pageTitle": "2019 &lt;b&gt;Honda Fit&lt;/b&gt; Prices, Incentives &amp;amp; Dealers | TrueCar",
        "partialMatchingImages": [
          {
            "url": "https://static.tcimg.net/vehicles/primary/15de1869a1c2ae12/2019-Honda-Fit-white-full_color-driver_side_front_quarter.png"
          },
          {
            "url": "https://static.tcimg.net/vehicles/primary/7efcf1db78a008cf/2019-Honda-Fit-white-full_color-driver_side_front_quarter.png"
          }
        ]
      },
      {
        "url": "https://www.orleanshonda.com/en/new/details/honda/fit/2018/sport/2505/7636",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; SPORT - Orléans Honda in Orléans",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w500c/images/newcar/2018/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          },
          {
            "url": "https://img.sm360.ca/images/newcar/2018/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "https://www.kbb.com/cars-for-sale/cars/honda/fit/",
        "pageTitle": "&lt;b&gt;Honda Fit&lt;/b&gt; Vehicles for Sale near Mountain View, CA 94035 | Kelley ...",
        "partialMatchingImages": [
          {
            "url": "https://file.kbb.com/kbb/vehicleimage/evoxseo/cp/m/12149/2018-honda-fit-front_12149_032_152x114_wa.png"
          }
        ]
      },
      {
        "url": "https://www.civicmotors.com/en/new/details/honda/fit/2018/sport-sensing/2505/7638",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; SPORT SENSING - Civic Motors Honda in Ottawa",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/images/newcar/2018/honda/fit/sport-sensing/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "https://www.brockvillehonda.com/en/new/details/honda/fit/2018/sport/2505/7636",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; SPORT - Brockville Honda in Brockville",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w500c/images/newcar/2018/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          },
          {
            "url": "https://img.sm360.ca/images/newcar/2018/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "https://www.hondavictoriaville.com/en/new/details/honda/fit/2019/lx/3034/9607",
        "pageTitle": "2019 &lt;b&gt;Honda Fit&lt;/b&gt; for sale in Victoriaville | &lt;b&gt;Honda&lt;/b&gt; Victoriaville",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w170/images/newcar/ca/2019/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "http://www.hondastnicolas.com/en/new/details/honda/fit/2018/lx/2505/7640",
        "pageTitle": "&lt;b&gt;Honda Fit LX 2018&lt;/b&gt; - &lt;b&gt;Honda&lt;/b&gt; St-Nicolas in Lévis, Quebec",
        "fullMatchingImages": [
          {
            "url": "http://img0.sm360.ca/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.hondavictoriaville.com/en/new/details/honda/fit/2019/dx/3034/9608",
        "pageTitle": "2019 &lt;b&gt;Honda Fit&lt;/b&gt; for sale in Victoriaville | &lt;b&gt;Honda&lt;/b&gt; Victoriaville",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w170/images/newcar/ca/2019/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "https://www.graingerhonda.com/vehicle-details/savannah-ga-new-2018-honda-fit-lx-VHF2018WA395311XX940",
        "pageTitle": "&lt;b&gt;2018 Honda Fit LX&lt;/b&gt; VHF2018WA395311XX | Grainger Honda ...",
        "fullMatchingImages": [
          {
            "url": "http://stock.fzautomotive.com/color_0640_032_png/my2018/12182/12182_cc0640_032_WA.png?404=nophoto.jpg"
          }
        ]
      },
      {
        "url": "http://www.spinellihonda.com/en/new-catalog/honda/2018-honda-fit-lx-id7640",
        "pageTitle": "New &lt;b&gt;2018 Honda Fit LX&lt;/b&gt; for sale in Montreal | Spinelli Honda Lachine",
        "fullMatchingImages": [
          {
            "url": "http://img0.sm360.ca/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.largohonda.com/vehicle-details/florida-city-fl-new-2018-honda-fit-lx-VHF2018WA395312XX",
        "pageTitle": "&lt;b&gt;2018 Honda Fit LX&lt;/b&gt; VHF2018WA395312XX | Largo Honda Florida ...",
        "fullMatchingImages": [
          {
            "url": "http://stock.fzautomotive.com/color_0640_032_png/my2018/12182/12182_cc0640_032_WA.png?404=nophoto.jpg"
          }
        ]
      },
      {
        "url": "https://www.hondaofjasper.com/new-inventory?Model=Fit",
        "pageTitle": "New &lt;b&gt;Hondas&lt;/b&gt; For Sale | &lt;b&gt;Fit&lt;/b&gt; Inventory | Jasper, Birmingham ...",
        "partialMatchingImages": [
          {
            "url": "https://cdn.getauto.com/photos/6/228766/1c/3HGGK5H43KM712064-1c.jpg?201901011825"
          }
        ]
      },
      {
        "url": "https://www.mierinsautomotivegroup.com/en/new/details/honda/fit/2018/sport/2505/7636",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; SPORT - Mierins Automotive Group in Ontario",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w500c/images/newcar/2018/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "https://www.supershonda.com/vehicle-details/mesa-az-new-2018-honda-fit-lx-VHF2018WA395311XX",
        "pageTitle": "&lt;b&gt;2018 Honda Fit LX&lt;/b&gt; VHF2018WA395311XX | Honda of Superstition ...",
        "fullMatchingImages": [
          {
            "url": "http://stock.fzautomotive.com/color_0640_032_png/my2018/12182/12182_cc0640_032_WA.png?404=nophoto.jpg"
          }
        ]
      },
      {
        "url": "https://www.lallierhondamontreal.com/en/new-catalog/honda/2018-honda-fit-sport-id7636",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; SPORT - Lallier Honda Montreal in Montréal",
        "partialMatchingImages": [
          {
            "url": "https://img2.sm360.ca/ir/w600h373c/images/newcar/2018/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "https://www.encorehonda.com/en/new-catalog/honda/2018-honda-fit-dx-id7637",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; DX - from $16845.0 | Encore Honda",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w640h390c/images/newcar/2018/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "https://www.bronxhonda.com/vehicle-details/bronx-ny-new-2018-honda-fit-lx-VHF2018WA395312XX",
        "pageTitle": "&lt;b&gt;2018 Honda Fit LX&lt;/b&gt; VHF2018WA395312XX | Bronx Honda Bronx, NY",
        "fullMatchingImages": [
          {
            "url": "http://stock.fzautomotive.com/color_0640_032_png/my2018/12182/12182_cc0640_032_WA.png?404=nophoto.jpg"
          }
        ]
      },
      {
        "url": "https://www.lallierhondahull.com/en/new/details/honda/fit/2018/sport/2505/7636",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; SPORT - Lallier Honda Hull in Gatineau",
        "partialMatchingImages": [
          {
            "url": "https://img2.sm360.ca/ir/w600h373c/images/newcar/2018/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "http://www.fundyhonda.com/en/new/details/honda/fit/2019/lx/3034/9607",
        "pageTitle": "New 2019 &lt;b&gt;Honda Fit LX&lt;/b&gt; at Fundy &lt;b&gt;Honda&lt;/b&gt;",
        "fullMatchingImages": [
          {
            "url": "http://img2.sm360.ca/images/newcar/ca/2019/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "https://www.encorehonda.com/en/new-catalog/honda/2018-honda-fit-sport-id7636",
        "pageTitle": "&lt;b&gt;2018 Honda Fit&lt;/b&gt; SPORT - from $21345.0 | Encore Honda",
        "partialMatchingImages": [
          {
            "url": "https://img.sm360.ca/ir/w640h390c/images/newcar/2018/honda/fit/sport/hatchback/exteriorColors/12149_cc0640_032_wa.png"
          }
        ]
      },
      {
        "url": "http://www.valleyfieldhonda.com/en/new/details/honda/fit/2018/lx/2505/7640",
        "pageTitle": "New &lt;b&gt;2018 Honda Fit LX&lt;/b&gt; at Valleyfield Honda",
        "fullMatchingImages": [
          {
            "url": "http://img0.sm360.ca/images/newcar/2018/honda/fit/lx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "http://www.automanichonda.com/en/new/details/honda/fit/2018/dx/2505/7637",
        "pageTitle": "Jean Dumas Honda | New &lt;b&gt;2018 Honda Fit&lt;/b&gt; DX for sale in Baie ...",
        "partialMatchingImages": [
          {
            "url": "http://img.sm360.ca/ir/w165c/images/newcar/2018/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      },
      {
        "url": "http://www.kingshonda.com/en/new/details/honda/fit/2018/dx/2505/7637",
        "pageTitle": "Kings County Honda | New &lt;b&gt;2018 Honda Fit&lt;/b&gt; DX for sale in Kentville",
        "fullMatchingImages": [
          {
            "url": "http://img.sm360.ca/images/newcar/2018/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
          }
        ]
      }
    ],
    "visuallySimilarImages": [
      {
        "url": "http://img1.sm360.ca/images/newcar/2018/honda/fit/dx/hatchback/exteriorColors/12182_cc0640_032_WA.png"
      },
      {
        "url": "https://www.fmdt.info/img/honda-models/2017-honda-fit-lx-32-white.png"
      },
      {
        "url": "https://joecampanale.com/wp-content/uploads/2017/12/New-2017-Honda-Fit-LX-Hatchback-for-sale-only-16965.-Visit-Honda-World-Downey-in-Downey-CA-serving-Los-Angeles-Whittier-and-Norwalk-2018-honda-fit-review-edmunds.jpg"
      },
      {
        "url": "https://img.sm360.ca/images/newcar/2018/honda/fit/lx/hatchback/12182_st0640_046.jpg"
      },
      {
        "url": "https://www.leasecosts.ca/sites/default/files/styles/large/public/2018-01/honda_canada_honda_fit_0.jpg?itok=z62MWAlo"
      },
      {
        "url": "https://nfmhof.com/wp-content/uploads/2018/11/new-honda-fit-cabin-air-filter-luxury-new-2016-honda-fit-lx-hatchback-in-glendale-and-luxury-honda-fit-cabin-air-filter.png"
      },
      {
        "url": "http://blogmedia.dealerfire.com/wp-content/uploads/sites/116/2017/07/2018-Honda-Fit-white-orchid_o-e1501256862812.jpg"
      },
      {
        "url": "https://sdhondadealers.com/media/models/227/2018-Honda-Fit-Lunar-Silver-Metallic-LX-Trim.png"
      }
    ],
    "bestGuessLabels": [
      {
        "label": "2018 honda fit lx white",
        "languageCode": "en"
      }
    ]
  }
}

    labels = label_list["labelAnnotations"]
    for index in range(len(labels)):
        #this is getting the useful info from the api dictionary
        cat = labels[index]['description']
        car_make = cat
        car_make_list = car_make.split()
        #list of valid car makes that the image api could guess
        makes = ['Acura','Audi','BMW','Cadillac','Chevrolet','Chrysler',
                 'Dodge','Eagle','Ferrari','Ford','Fiat','GMC','Honda','Hummer','Hyundai',
                 'Infiniti','Isuzu','Jaguar','Jeep','Kia','Lamborghini','Land rover',
                 'Lexus','Lincoln','Lotus','Mazda','Mercedes-benz','Mercury','Mitsubishi',
                 'Nissan','Oldsmobile','Peugeot','Porsche','Buick','Sabb','Saturn','Subaru'
                 ,'Suzuki','Toyota','Volkswagon','Volvo']
        #if the image is seeing something thats not a car brand
        if car_make_list[0] not in makes:
            pass
        #if its less than two strings then it's not going to be a make and model pair
        elif len(car_make_list) < 2:
            pass
        #this entire loop searches through the list making sure it's a valid vehicle combination
        else:
            for item in car_make_list:
                c = car_make_list[1][0].upper()
                car = c + car_make_list[1][1:]
                car_make_list[1] = car
            model = car_make_list[1]
            dict = get_json('https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/' + car_make_list[0] +'/modelyear/2015?format=json')
            results = dict['Results']
            models = []
            for index in range(len(results)):
                models.append(results[index]['Model_Name'])
            #checking if the make found has a valid model name
            if model in models:
                print('Valid Car ' + cat)
            else:
                pass

    #checking runtime
    end = time.time()
    print((round(end-start,2)), 'seconds')

if __name__ == '__main__':
    main()