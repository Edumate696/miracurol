/*global angular*/

'use strict';

angular.module('miracurolApp', ['ui.router'])
    .config(function ($stateProvider, $locationProvider, $urlRouterProvider) {
        // Enable HTML-5 Mode
        $locationProvider.html5Mode({
            enabled: true, requireBase: false
        });

        // Default to 'https://<base url>/'
        $urlRouterProvider.otherwise('/');

        // creating routes or states
        $stateProvider
            .state({
                name: 'home', url: '/', views: {
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