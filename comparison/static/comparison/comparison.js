(function ($) {

    ComparisonButton = function ($btn) {

        var self = this;

        this._toggleLoading = function (isVisible) {
            $btn.find('[data-role=loading]')[isVisible ? 'show' : 'hide']();
            $btn.find('[data-role=comparison-remove]')[isVisible ? 'hide' : 'show']();
            $btn.find('[data-role=comparison-add]')[isVisible ? 'hide' : 'show']();
        };

        this._toggleComparison = function (isActive) {
            $btn.find('[data-role=comparison-remove]')[isActive ? 'show' : 'hide']();
            $btn.find('[data-role=comparison-add]')[isActive ? 'hide' : 'show']();
        };

        this._toggleLoading(false);
        this._toggleComparison($btn.data('active'));

        $btn.click(function () {
            $btn.prop('disabled', true);
            self._toggleLoading(true);

            $.post($btn.data('url'), function (response) {
                self._toggleLoading(false);
                $btn.prop('disabled', false);
                self._toggleComparison(response.is_active);
                $('[data-role=comparison-dropdown]').html(response.dropdown);
                $.notify({message: response.message}, {type: 'success'});
            });
        });
    }

})(jQuery);