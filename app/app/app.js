(function () {
    'use strict';

    const app = angular.module('miracurolApp', ['ui.router']);

    app.config(function ($stateProvider, $locationProvider) {
        // Enable HTML-5 Mode
        $locationProvider.html5Mode({
            enabled: true, requireBase: false
        });

        // creating routes or states
        $stateProvider
            .state({
                name: 'home', views: {
                    "content": {
                        template: '<h1 class="mt-4">This is Home Page</h1>',
                    }
                },
            })
            .state({
                name: 'about', views: {
                    "content": {
                        template: '<h1 class="mt-4">This is About Page</h1>',
                    }
                },
            });
    });

    app.run(function ($state) {
        $state.go('home');
    });

    return app;
}());