{
  'targets': [
    {
      'win_delay_load_hook': 'true',
      'target_name': 'bson',
      'sources': [ 'src/bson.cc' ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'include_dirs': [ '<!(node -e "require(\'nan\')")' ],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CFLAGS': [
              '-O3',
              '-msse2',
              '-ffast-math',
              '-fexceptions'
            ]
          }
        }],
        ['OS=="win"', {
          'msvs_settings': {
            'VCCLCompilerTool': {
              'ExceptionHandling': 1
            }
          }
        }],
        ['OS=="linux"', {
          "cflags": [
            "-O3",
            "-msse2",
            "-ffast-math",
            "-fexceptions"
          ]
        }]
      ]
    }
  ]
}
