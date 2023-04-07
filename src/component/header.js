import React from 'react'

export default function header() {
    return ( <
        nav class = "navbar navbar-expand-lg bg-body-tertiary" >
        <
        div class = "container-fluid" >
        <
        a class = "navbar-brand"
        href = "#" > Real - time Hospital Management System < /a> <
        button class = "navbar-toggler"
        type = "button"
        data - bs - toggle = "collapse"
        data - bs - target = "#navbarSupportedContent"
        aria - controls = "navbarSupportedContent"
        aria - expanded = "false"
        aria - label = "Toggle navigation" >
        <
        span class = "navbar-toggler-icon" > < /span> <
        /button> <
        div class = "collapse navbar-collapse"
        id = "navbarSupportedContent" >
        <
        ul class = "navbar-nav me-auto mb-2 mb-lg-0" >

        <
        li class = "nav-item dropdown" >
        <
        a class = "nav-link dropdown-toggle"
        href = "#"
        role = "button"
        data - bs - toggle = "dropdown"
        aria - expanded = "false" >
        Reception Side <
        /a> <
        ul class = "dropdown-menu" >
        <
        li > < a class = "dropdown-item"
        href = "#" > Prescription Display < /a></li >
        <
        li > < a class = "dropdown-item"
        href = "#" > Reports Display < /a></li >
        <
        li > < hr class = "dropdown-divider" / > < /li> <
        li > < a class = "dropdown-item"
        href = "#" > EMERGENCY < /a></li >
        <
        /ul> <
        /li> <
        li class = "nav-item" >
        <
        a class = "nav-link active"
        aria - current = "page"
        href = "#" > Doctor Side Display < /a> <
        /li> <
        li class = "nav-item" >
        <
        a class = "nav-link disabled" > EMERGENCY < /a> <
        /li> <
        /ul> <
        form class = "d-flex"
        role = "search" >
        <
        input class = "form-control me-2"
        type = "search"
        placeholder = "Search"
        aria - label = "Search" / >
        <
        button class = "btn btn-outline-success"
        type = "submit" > Search < /button> <
        /form> <
        /div> <
        /div> <
        /nav>
    )
}