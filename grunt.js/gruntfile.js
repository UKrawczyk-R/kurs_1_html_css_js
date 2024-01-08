module.exports = function(grunt){
    //project configuration
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        
            autoprefixer: {
              options: {
                browsers: ['last 2 versions', 'ie 8', 'ie 9']
              },
              dist: { //najczesciej sie pisze dist jednak mozna uzyc jakiejkolwiek innej nawzy
               src: 'css/style.css',
               dest: 'css/styleprefixed.css'
              }
            },
            watch:
            {
                autoprefixer: //jezeli chcemy obserwowac wiecej niz jeden plik nadajemy etykiete np. autoprefixer
               {
                files: 'css/style.css',
                tasks: ['autoprefixer']  //po przecinku mozna dodac task
               }

            },
            cssmin:
            {
                target:
                {
                    files:
                    {
                        'css/styleprefixed.min.css': ['css/styleprefixed.css'] // pierwsze nazwa pliku w któym bedzie cssmin w klamrach pliki z których bedzie tworzony css min jezli jest wiwecej niz jeden plik css to je wpsiujemy po przecinku i je połączy w 1.
                    }
                }
            }
          
    });

    grunt.loadNpmTasks('grunt-autoprefixer');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    grunt.registerTask("default", ['autoprefixer', 'watch','cssmin']);

   // grunt.registerTask("nazwaWlasna", "opis tego co sie tu zdarza", ['autoprefixer']);

};