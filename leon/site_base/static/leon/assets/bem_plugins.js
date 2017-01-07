(function ($, class_bus) {

    "use strict";

    /**
     * Class of custom modifiers applying (BEM)
     * */
    class_bus.BemBlocksModify = function () {

        this.setModifiers = function (modifiers) {
            $.each(modifiers, function (index, cell) {
                var block = cell['block'];
                var modifier = cell['modifier'];
                $(block).addClass(modifier);
            });
        };
    };
})(jQuery, jBus);
