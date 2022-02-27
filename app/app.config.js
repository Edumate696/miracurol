/*global angular*/

"use strict";

angular.module('miracurolApp', ['ui.router'])
    .config(function ($stateProvider, $locationProvider, $urlRouterProvider) {
        $locationProvider.html5Mode({
            enabled: true,
            requireBase: false
        });
        // $urlRouterProvider.otherwise('/');

        // creating routes or states
        $stateProvider
            .state({
                name: 'home',
                url: '/',
                views: {
                    "content": {
                        template: '<h1>This is Home Page</h1>',
                    }
                },
            })
            .state({
                name: 'about',
                views: {
                    "content": {
                        template: '<h1>This is About Page</h1>',
                    }
                },
            });
    });