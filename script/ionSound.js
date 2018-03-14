/**
 * Engine.js
 * © 2014 Denis Ineshin | IonDen.com
 */

$(function () {
console.log('ion sounds'); 	
    ion.sound({
        sounds: [
            {name: "beer_can_opening"},
            {name: "bell_ring", volume: 1},
            {name: "branch_break", volume: 0.3},
            {name: "button_click"},
            {name: "button_click_on"},
            {name: "button_push"},
            {name: "button_tiny", volume: 0.6},
            {name: "camera_flashing"},
            {name: "camera_flashing_2"},
            {name: "cd_tray"},
            {name: "computer_error"},
            {name: "door_bell"},
            {name: "door_bump", volume: 0.3},
            {name: "glass"},
            {name: "keyboard_desk"},
            {name: "light_bulb_breaking", volume: 0.2},
            {name: "metal_plate"},
            {name: "metal_plate_2"},
            {name: "pop_cork"},
            {name: "snap"},
            {name: "staple_gun"},
            {name: "tap"},
            {name: "water_droplet"},
            {name: "water_droplet_2"},
            {name: "water_droplet_3"}
        ],
        path: "./script/vendor/ion.sound-2.1.3/sounds/",
        preload: true
    });

    $("#b01").on("click", function () {
	console.log('bear sound');
	ion.sound.play("beer_can_opening");
    });
    $("#b02").on("click", function () {
        ion.sound.play("bell_ring");
    });
    $("#b03").on("click", function () {
        ion.sound.play("branch_break");
    });
    $("#b04").on("click", function () {
        ion.sound.play("button_click");
    });
    $("#b05").on("click", function () {
        ion.sound.play("button_click_on");
    });
    $("#b06").on("click", function () {
        ion.sound.play("button_push");
    });
    $("#b07").on("click", function () {
        ion.sound.play("button_tiny");
    });
    $("#b-camera-1").on("click", function () {
        ion.sound.play("camera_flashing");
    });
    $("#b-camera-2").on("click", function () {
        ion.sound.play("camera_flashing_2");
    });
    $("#b-cdtray").on("click", function () {
        ion.sound.play("cd_tray");
    });
    $("#b10").on("click", function () {
        ion.sound.play("computer_error");
    });
    $("#b-door").on("click", function () {
        ion.sound.play("door_bump");
    });
    $("#b-glass").on("click", function () {
        ion.sound.play("glass");
    });
    $("#b-keyboard").on("click", function () {
        ion.sound.play("keyboard_desk");
    });
    $("#b11").on("click", function () {
        ion.sound.play("door_bell");
    });
    $("#b12").on("click", function () {
        ion.sound.play("light_bulb_breaking");
    });
    $("#b-metal-1").on("click", function () {
        ion.sound.play("metal_plate");
    });
    $("#b-metal-2").on("click", function () {
        ion.sound.play("metal_plate_2");
    });
    $("#b14").on("click", function () {
        ion.sound.play("pop_cork");
    });
    $("#b-snap").on("click", function () {
        ion.sound.play("snap");
    });
    $("#b-staple").on("click", function () {
        ion.sound.play("staple_gun");
    });
    $("#b-tap").on("click", function () {
        ion.sound.play("tap");
    });
    $("#b-water-1").on("click", function () {
        ion.sound.play("water_droplet");
    });
    $("#b-water-2").on("click", function () {
        ion.sound.play("water_droplet_2");
    });
    $("#b-water-3").on("click", function () {
        ion.sound.play("water_droplet_3");
    });

    // keyboard
    $(document.body).on("keypress", function (e) {
        var key = e.which,
            $key_ico = $("q.key");

        var clearAll = function () {
            clearTimeout(window.myTm);

            window.myTm = setTimeout(function () {
                $key_ico.removeClass("key_state_active");
            }, 200);
        };

        if (/^(81|113|1049|1081)$/.test(key)) {         // Q
            ion.sound.play("beer_can_opening");
            $("#key_q").addClass("key_state_active");
            clearAll();
        } else if (/^(87|119|1062|1094)$/.test(key)) {  // W
            ion.sound.play("bell_ring");
            $("#key_w").addClass("key_state_active");
            clearAll();
        } else if (/^(69|101|1059|1091)$/.test(key)) {  // E
            ion.sound.play("branch_break");
            $("#key_e").addClass("key_state_active");
            clearAll();
        } else if (/^(81|114|1050|1082)$/.test(key)) {  // R
            ion.sound.play("button_click");
            $("#key_r").addClass("key_state_active");
            clearAll();
        } else if (/^(84|116|1045|1077)$/.test(key)) {  // T
            ion.sound.play("button_click_on");
            $("#key_t").addClass("key_state_active");
            clearAll();
        } else if (/^(89|121|1053|1085)$/.test(key)) {  // Y
            ion.sound.play("button_push");
            $("#key_y").addClass("key_state_active");
            clearAll();
        } else if (/^(85|117|1043|1075)$/.test(key)) {  // U
            ion.sound.play("button_tiny");
            $("#key_u").addClass("key_state_active");
            clearAll();
        } else if (/^(73|105|1064|1096)$/.test(key)) {  // I
            ion.sound.play("camera_flashing");
            $("#key_i").addClass("key_state_active");
            clearAll();
        } else if (/^(79|111|1065|1097)$/.test(key)) {  // O
            ion.sound.play("camera_flashing_2");
            $("#key_o").addClass("key_state_active");
            clearAll();
        } else if (/^(80|112|1047|1079)$/.test(key)) {  // P
            ion.sound.play("cd_tray");
            $("#key_p").addClass("key_state_active");
            clearAll();
        } else if (/^(65|97|1060|1092)$/.test(key)) {   // A
            ion.sound.play("computer_error");
            $("#key_a").addClass("key_state_active");
            clearAll();
        } else if (/^(83|115|1067|1099)$/.test(key)) {  // S
            ion.sound.play("door_bump");
            $("#key_s").addClass("key_state_active");
            clearAll();
        } else if (/^(68|100|1042|1074)$/.test(key)) {  // D
            ion.sound.play("glass");
            $("#key_d").addClass("key_state_active");
            clearAll();
        } else if (/^(70|102|1040|1072)$/.test(key)) {  // F
            ion.sound.play("keyboard_desk");
            $("#key_f").addClass("key_state_active");
            clearAll();
        } else if (/^(71|103|1055|1087)$/.test(key)) {  // G
            ion.sound.play("door_bell");
            $("#key_g").addClass("key_state_active");
            clearAll();
        } else if (/^(72|104|1056|1088)$/.test(key)) {  // H
            ion.sound.play("light_bulb_breaking");
            $("#key_h").addClass("key_state_active");
            clearAll();
        } else if (/^(74|106|1054|1086)$/.test(key)) {  // J
            ion.sound.play("metal_plate");
            $("#key_j").addClass("key_state_active");
            clearAll();
        } else if (/^(75|107|1051|1083)$/.test(key)) {  // K
            ion.sound.play("metal_plate_2");
            $("#key_k").addClass("key_state_active");
            clearAll();
        } else if (/^(76|108|1044|1076)$/.test(key)) {  // L
            ion.sound.play("pop_cork");
            $("#key_l").addClass("key_state_active");
            clearAll();
        } else if (/^(90|122|1071|1103)$/.test(key)) {  // Z
            ion.sound.play("snap");
            $("#key_z").addClass("key_state_active");
            clearAll();
        } else if (/^(88|120|1063|1095)$/.test(key)) {  // X
            ion.sound.play("staple_gun");
            $("#key_x").addClass("key_state_active");
            clearAll();
        } else if (/^(67|99|1057|1089)$/.test(key)) {   // C
            ion.sound.play("tap");
            $("#key_c").addClass("key_state_active");
            clearAll();
        } else if (/^(86|118|1052|1084)$/.test(key)) {  // V
            ion.sound.play("water_droplet");
            $("#key_v").addClass("key_state_active");
            clearAll();
        } else if (/^(66|98|1048|1080)$/.test(key)) {   // B
            ion.sound.play("water_droplet_2");
            $("#key_b").addClass("key_state_active");
            clearAll();
        } else if (/^(78|110|1058|1090)$/.test(key)) {  // N
            ion.sound.play("water_droplet_3");
            $("#key_n").addClass("key_state_active");
            clearAll();
        }

    });


    $(".js-volume").on("click", function (e) {
        e.preventDefault();
        var volume = $(this).data("volume");
        ion.sound.play("bell_ring", {
            volume: volume
        });
    });


    $(".js-play").on("click", function (e) {
        e.preventDefault();
        ion.sound.play("cd_tray", {
            volume: 1.0
        });
    });
    $(".js-stop").on("click", function (e) {
        e.preventDefault();
        ion.sound.stop("cd_tray");
    });


    $(".js-p-play").on("click", function (e) {
        e.preventDefault();
        ion.sound.play("cd_tray", {
            volume: 1.0,
            loop: 3
        });
    });
    $(".js-p-pause").on("click", function (e) {
        e.preventDefault();
        ion.sound.pause("cd_tray");
    });


    $(".js-loop-play").on("click", function (e) {
        e.preventDefault();
        ion.sound.play("glass", {
            volume: 0.6,
            loop: true
        });
    });
    $(".js-loop-stop").on("click", function (e) {
        e.preventDefault();
        ion.sound.stop("glass");
    });


    $(".js-loop5-play").on("click", function (e) {
        e.preventDefault();
        ion.sound.play("tap", {
            volume: 0.6,
            loop: 5
        });
    });
    $(".js-loop5-stop").on("click", function (e) {
        e.preventDefault();
        ion.sound.stop("tap");
    });


    $(".js-kill").on("click", function (e) {
        e.preventDefault();
        var name = $(this).data("name");
        if (name) {
            ion.sound.destroy(name);
        } else {
            ion.sound.destroy();
        }
    });

});
