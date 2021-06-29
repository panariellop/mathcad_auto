
/* Code to register embedded modules for meta path based loading if any. */

#include <Python.h>

#include "nuitka/constants_blob.h"

#include "nuitka/unfreezing.h"

/* Type bool */
#ifndef __cplusplus
#include "stdbool.h"
#endif

#if 0 > 0
static unsigned char *bytecode_data[0];
#else
static unsigned char **bytecode_data = NULL;
#endif

/* Table for lookup to find compiled or bytecode modules included in this
 * binary or module, or put along this binary as extension modules. We do
 * our own loading for each of these.
 */
extern PyObject *modulecode_MathcadPy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_MathcadPy$__version__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_MathcadPy$_application(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$BmpImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$GifImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$GimpGradientFile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$GimpPaletteFile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$Image(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageChops(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageColor(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageFile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageFilter(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageMode(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImagePalette(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageQt(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageSequence(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageShow(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$JpegImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$JpegPresets(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$MpoImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$PaletteFile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$PngImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$PpmImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$PyAccess(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$TiffImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$TiffTags(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$_binary(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$_util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PySimpleGUI(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PySimpleGUI$PySimpleGUI(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode___main__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_commctrl(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_et_xmlfile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_et_xmlfile$xmlfile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_images(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$_constants(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$cell(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$cell$_writer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$cell$cell(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$cell$read_only(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$cell$text(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$_3d(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$_chart(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$area_chart(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$axis(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$bar_chart(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$bubble_chart(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$chartspace(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$data_source(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$descriptors(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$error_bar(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$label(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$layout(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$legend(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$line_chart(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$marker(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$picture(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$pie_chart(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$pivot(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$plotarea(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$print_settings(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$radar_chart(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$reader(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$reference(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$scatter_chart(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$series(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$series_factory(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$shapes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$stock_chart(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$surface_chart(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$text(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$title(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$trendline(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chart$updown_bars(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chartsheet(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chartsheet$chartsheet(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chartsheet$custom(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chartsheet$properties(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chartsheet$protection(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chartsheet$publish(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chartsheet$relation(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$chartsheet$views(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$comments(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$comments$author(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$comments$comment_sheet(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$comments$comments(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$comments$shape_writer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$compat$numbers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$compat$strings(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$descriptors(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$descriptors$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$descriptors$excel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$descriptors$namespace(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$descriptors$nested(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$descriptors$sequence(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$descriptors$serialisable(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$colors(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$connector(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$drawing(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$effect(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$fill(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$geometry(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$graphic(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$image(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$line(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$picture(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$properties(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$relation(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$spreadsheet_drawing(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$text(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$drawing$xdr(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$formatting(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$formatting$formatting(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$formatting$rule(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$formula(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$formula$tokenizer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$formula$translate(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$packaging(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$packaging$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$packaging$extended(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$packaging$manifest(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$packaging$relationship(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$packaging$workbook(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$pivot(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$pivot$cache(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$pivot$fields(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$pivot$record(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$pivot$table(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$reader(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$reader$drawings(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$reader$excel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$reader$strings(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$reader$workbook(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$alignment(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$borders(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$builtins(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$cell_style(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$colors(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$differential(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$fills(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$fonts(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$named_styles(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$numbers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$protection(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$proxy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$styleable(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$stylesheet(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$styles$table(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$utils$bound_dictionary(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$utils$cell(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$utils$datetime(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$utils$escape(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$utils$exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$utils$formulas(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$utils$indexed_list(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$utils$protection(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$utils$units(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$_writer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$child(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$defined_name(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$external_link(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$external_link$external(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$external_reference(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$function_group(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$properties(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$protection(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$smart_tags(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$views(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$web(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$workbook$workbook(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$_read_only(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$_reader(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$_write_only(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$_writer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$cell_range(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$copier(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$datavalidation(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$dimensions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$drawing(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$filters(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$header_footer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$hyperlink(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$merge(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$page(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$pagebreak(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$properties(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$protection(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$related(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$scenario(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$table(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$views(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$worksheet$worksheet(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$writer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$writer$excel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$writer$theme(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$xml(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$xml$constants(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl$xml$functions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl_image_loader(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_openpyxl_image_loader$sheet_image_loader(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyperclip(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pythoncom(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$dialogs(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$dialogs$list(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$dialogs$status(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$mfc(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$mfc$dialog(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$mfc$object(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$mfc$thread(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$mfc$window(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin32_bootstrap(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin32_system32(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywintypes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$CLSIDToClass(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$build(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$dynamic(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$gencache(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$genpy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$makepy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$selecttlb(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32con(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_winerror(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);

static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] = {
    {"MathcadPy", modulecode_MathcadPy, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"MathcadPy.__version__", modulecode_MathcadPy$__version__, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"MathcadPy._application", modulecode_MathcadPy$_application, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL", modulecode_PIL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"PIL.BmpImagePlugin", modulecode_PIL$BmpImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.GifImagePlugin", modulecode_PIL$GifImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.GimpGradientFile", modulecode_PIL$GimpGradientFile, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.GimpPaletteFile", modulecode_PIL$GimpPaletteFile, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.Image", modulecode_PIL$Image, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageChops", modulecode_PIL$ImageChops, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageColor", modulecode_PIL$ImageColor, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageFile", modulecode_PIL$ImageFile, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageFilter", modulecode_PIL$ImageFilter, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageMode", modulecode_PIL$ImageMode, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImagePalette", modulecode_PIL$ImagePalette, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageQt", modulecode_PIL$ImageQt, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageSequence", modulecode_PIL$ImageSequence, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageShow", modulecode_PIL$ImageShow, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.JpegImagePlugin", modulecode_PIL$JpegImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.JpegPresets", modulecode_PIL$JpegPresets, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.MpoImagePlugin", modulecode_PIL$MpoImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.PaletteFile", modulecode_PIL$PaletteFile, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.PngImagePlugin", modulecode_PIL$PngImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.PpmImagePlugin", modulecode_PIL$PpmImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.PyAccess", modulecode_PIL$PyAccess, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.TiffImagePlugin", modulecode_PIL$TiffImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.TiffTags", modulecode_PIL$TiffTags, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL._binary", modulecode_PIL$_binary, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL._util", modulecode_PIL$_util, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL._version", modulecode_PIL$_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PySimpleGUI", modulecode_PySimpleGUI, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"PySimpleGUI.PySimpleGUI", modulecode_PySimpleGUI$PySimpleGUI, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"__main__", modulecode___main__, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"commctrl", modulecode_commctrl, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"et_xmlfile", modulecode_et_xmlfile, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"et_xmlfile.xmlfile", modulecode_et_xmlfile$xmlfile, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"images", modulecode_images, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl", modulecode_openpyxl, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl._constants", modulecode_openpyxl$_constants, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.cell", modulecode_openpyxl$cell, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.cell._writer", modulecode_openpyxl$cell$_writer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.cell.cell", modulecode_openpyxl$cell$cell, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.cell.read_only", modulecode_openpyxl$cell$read_only, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.cell.text", modulecode_openpyxl$cell$text, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart", modulecode_openpyxl$chart, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.chart._3d", modulecode_openpyxl$chart$_3d, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart._chart", modulecode_openpyxl$chart$_chart, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.area_chart", modulecode_openpyxl$chart$area_chart, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.axis", modulecode_openpyxl$chart$axis, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.bar_chart", modulecode_openpyxl$chart$bar_chart, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.bubble_chart", modulecode_openpyxl$chart$bubble_chart, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.chartspace", modulecode_openpyxl$chart$chartspace, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.data_source", modulecode_openpyxl$chart$data_source, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.descriptors", modulecode_openpyxl$chart$descriptors, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.error_bar", modulecode_openpyxl$chart$error_bar, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.label", modulecode_openpyxl$chart$label, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.layout", modulecode_openpyxl$chart$layout, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.legend", modulecode_openpyxl$chart$legend, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.line_chart", modulecode_openpyxl$chart$line_chart, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.marker", modulecode_openpyxl$chart$marker, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.picture", modulecode_openpyxl$chart$picture, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.pie_chart", modulecode_openpyxl$chart$pie_chart, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.pivot", modulecode_openpyxl$chart$pivot, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.plotarea", modulecode_openpyxl$chart$plotarea, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.print_settings", modulecode_openpyxl$chart$print_settings, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.radar_chart", modulecode_openpyxl$chart$radar_chart, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.reader", modulecode_openpyxl$chart$reader, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.reference", modulecode_openpyxl$chart$reference, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.scatter_chart", modulecode_openpyxl$chart$scatter_chart, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.series", modulecode_openpyxl$chart$series, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.series_factory", modulecode_openpyxl$chart$series_factory, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.shapes", modulecode_openpyxl$chart$shapes, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.stock_chart", modulecode_openpyxl$chart$stock_chart, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.surface_chart", modulecode_openpyxl$chart$surface_chart, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.text", modulecode_openpyxl$chart$text, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.title", modulecode_openpyxl$chart$title, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.trendline", modulecode_openpyxl$chart$trendline, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chart.updown_bars", modulecode_openpyxl$chart$updown_bars, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chartsheet", modulecode_openpyxl$chartsheet, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.chartsheet.chartsheet", modulecode_openpyxl$chartsheet$chartsheet, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chartsheet.custom", modulecode_openpyxl$chartsheet$custom, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chartsheet.properties", modulecode_openpyxl$chartsheet$properties, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chartsheet.protection", modulecode_openpyxl$chartsheet$protection, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chartsheet.publish", modulecode_openpyxl$chartsheet$publish, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chartsheet.relation", modulecode_openpyxl$chartsheet$relation, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.chartsheet.views", modulecode_openpyxl$chartsheet$views, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.comments", modulecode_openpyxl$comments, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.comments.author", modulecode_openpyxl$comments$author, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.comments.comment_sheet", modulecode_openpyxl$comments$comment_sheet, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.comments.comments", modulecode_openpyxl$comments$comments, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.comments.shape_writer", modulecode_openpyxl$comments$shape_writer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.compat", modulecode_openpyxl$compat, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.compat.numbers", modulecode_openpyxl$compat$numbers, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.compat.strings", modulecode_openpyxl$compat$strings, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.descriptors", modulecode_openpyxl$descriptors, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.descriptors.base", modulecode_openpyxl$descriptors$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.descriptors.excel", modulecode_openpyxl$descriptors$excel, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.descriptors.namespace", modulecode_openpyxl$descriptors$namespace, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.descriptors.nested", modulecode_openpyxl$descriptors$nested, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.descriptors.sequence", modulecode_openpyxl$descriptors$sequence, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.descriptors.serialisable", modulecode_openpyxl$descriptors$serialisable, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing", modulecode_openpyxl$drawing, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.drawing.colors", modulecode_openpyxl$drawing$colors, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.connector", modulecode_openpyxl$drawing$connector, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.drawing", modulecode_openpyxl$drawing$drawing, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.effect", modulecode_openpyxl$drawing$effect, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.fill", modulecode_openpyxl$drawing$fill, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.geometry", modulecode_openpyxl$drawing$geometry, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.graphic", modulecode_openpyxl$drawing$graphic, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.image", modulecode_openpyxl$drawing$image, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.line", modulecode_openpyxl$drawing$line, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.picture", modulecode_openpyxl$drawing$picture, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.properties", modulecode_openpyxl$drawing$properties, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.relation", modulecode_openpyxl$drawing$relation, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.spreadsheet_drawing", modulecode_openpyxl$drawing$spreadsheet_drawing, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.text", modulecode_openpyxl$drawing$text, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.drawing.xdr", modulecode_openpyxl$drawing$xdr, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.formatting", modulecode_openpyxl$formatting, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.formatting.formatting", modulecode_openpyxl$formatting$formatting, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.formatting.rule", modulecode_openpyxl$formatting$rule, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.formula", modulecode_openpyxl$formula, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.formula.tokenizer", modulecode_openpyxl$formula$tokenizer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.formula.translate", modulecode_openpyxl$formula$translate, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.packaging", modulecode_openpyxl$packaging, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.packaging.core", modulecode_openpyxl$packaging$core, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.packaging.extended", modulecode_openpyxl$packaging$extended, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.packaging.manifest", modulecode_openpyxl$packaging$manifest, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.packaging.relationship", modulecode_openpyxl$packaging$relationship, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.packaging.workbook", modulecode_openpyxl$packaging$workbook, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.pivot", modulecode_openpyxl$pivot, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.pivot.cache", modulecode_openpyxl$pivot$cache, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.pivot.fields", modulecode_openpyxl$pivot$fields, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.pivot.record", modulecode_openpyxl$pivot$record, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.pivot.table", modulecode_openpyxl$pivot$table, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.reader", modulecode_openpyxl$reader, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.reader.drawings", modulecode_openpyxl$reader$drawings, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.reader.excel", modulecode_openpyxl$reader$excel, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.reader.strings", modulecode_openpyxl$reader$strings, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.reader.workbook", modulecode_openpyxl$reader$workbook, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles", modulecode_openpyxl$styles, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.styles.alignment", modulecode_openpyxl$styles$alignment, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.borders", modulecode_openpyxl$styles$borders, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.builtins", modulecode_openpyxl$styles$builtins, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.cell_style", modulecode_openpyxl$styles$cell_style, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.colors", modulecode_openpyxl$styles$colors, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.differential", modulecode_openpyxl$styles$differential, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.fills", modulecode_openpyxl$styles$fills, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.fonts", modulecode_openpyxl$styles$fonts, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.named_styles", modulecode_openpyxl$styles$named_styles, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.numbers", modulecode_openpyxl$styles$numbers, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.protection", modulecode_openpyxl$styles$protection, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.proxy", modulecode_openpyxl$styles$proxy, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.styleable", modulecode_openpyxl$styles$styleable, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.stylesheet", modulecode_openpyxl$styles$stylesheet, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.styles.table", modulecode_openpyxl$styles$table, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.utils", modulecode_openpyxl$utils, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.utils.bound_dictionary", modulecode_openpyxl$utils$bound_dictionary, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.utils.cell", modulecode_openpyxl$utils$cell, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.utils.datetime", modulecode_openpyxl$utils$datetime, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.utils.escape", modulecode_openpyxl$utils$escape, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.utils.exceptions", modulecode_openpyxl$utils$exceptions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.utils.formulas", modulecode_openpyxl$utils$formulas, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.utils.indexed_list", modulecode_openpyxl$utils$indexed_list, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.utils.protection", modulecode_openpyxl$utils$protection, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.utils.units", modulecode_openpyxl$utils$units, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.workbook", modulecode_openpyxl$workbook, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.workbook._writer", modulecode_openpyxl$workbook$_writer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.workbook.child", modulecode_openpyxl$workbook$child, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.workbook.defined_name", modulecode_openpyxl$workbook$defined_name, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.workbook.external_link", modulecode_openpyxl$workbook$external_link, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.workbook.external_link.external", modulecode_openpyxl$workbook$external_link$external, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.workbook.external_reference", modulecode_openpyxl$workbook$external_reference, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.workbook.function_group", modulecode_openpyxl$workbook$function_group, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.workbook.properties", modulecode_openpyxl$workbook$properties, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.workbook.protection", modulecode_openpyxl$workbook$protection, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.workbook.smart_tags", modulecode_openpyxl$workbook$smart_tags, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.workbook.views", modulecode_openpyxl$workbook$views, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.workbook.web", modulecode_openpyxl$workbook$web, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.workbook.workbook", modulecode_openpyxl$workbook$workbook, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet", modulecode_openpyxl$worksheet, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.worksheet._read_only", modulecode_openpyxl$worksheet$_read_only, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet._reader", modulecode_openpyxl$worksheet$_reader, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet._write_only", modulecode_openpyxl$worksheet$_write_only, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet._writer", modulecode_openpyxl$worksheet$_writer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.cell_range", modulecode_openpyxl$worksheet$cell_range, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.copier", modulecode_openpyxl$worksheet$copier, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.datavalidation", modulecode_openpyxl$worksheet$datavalidation, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.dimensions", modulecode_openpyxl$worksheet$dimensions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.drawing", modulecode_openpyxl$worksheet$drawing, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.filters", modulecode_openpyxl$worksheet$filters, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.header_footer", modulecode_openpyxl$worksheet$header_footer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.hyperlink", modulecode_openpyxl$worksheet$hyperlink, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.merge", modulecode_openpyxl$worksheet$merge, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.page", modulecode_openpyxl$worksheet$page, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.pagebreak", modulecode_openpyxl$worksheet$pagebreak, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.properties", modulecode_openpyxl$worksheet$properties, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.protection", modulecode_openpyxl$worksheet$protection, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.related", modulecode_openpyxl$worksheet$related, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.scenario", modulecode_openpyxl$worksheet$scenario, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.table", modulecode_openpyxl$worksheet$table, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.views", modulecode_openpyxl$worksheet$views, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.worksheet.worksheet", modulecode_openpyxl$worksheet$worksheet, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.writer", modulecode_openpyxl$writer, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.writer.excel", modulecode_openpyxl$writer$excel, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.writer.theme", modulecode_openpyxl$writer$theme, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.xml", modulecode_openpyxl$xml, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl.xml.constants", modulecode_openpyxl$xml$constants, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl.xml.functions", modulecode_openpyxl$xml$functions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"openpyxl_image_loader", modulecode_openpyxl_image_loader, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"openpyxl_image_loader.sheet_image_loader", modulecode_openpyxl_image_loader$sheet_image_loader, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyperclip", modulecode_pyperclip, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pythoncom", modulecode_pythoncom, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pywin", modulecode_pywin, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pywin.dialogs", modulecode_pywin$dialogs, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pywin.dialogs.list", modulecode_pywin$dialogs$list, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pywin.dialogs.status", modulecode_pywin$dialogs$status, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pywin.mfc", modulecode_pywin$mfc, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pywin.mfc.dialog", modulecode_pywin$mfc$dialog, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pywin.mfc.object", modulecode_pywin$mfc$object, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pywin.mfc.thread", modulecode_pywin$mfc$thread, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pywin.mfc.window", modulecode_pywin$mfc$window, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pywin32_bootstrap", modulecode_pywin32_bootstrap, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pywin32_system32", modulecode_pywin32_system32, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pywintypes", modulecode_pywintypes, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"win32com", modulecode_win32com, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"win32com.client", modulecode_win32com$client, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"win32com.client.CLSIDToClass", modulecode_win32com$client$CLSIDToClass, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"win32com.client.build", modulecode_win32com$client$build, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"win32com.client.dynamic", modulecode_win32com$client$dynamic, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"win32com.client.gencache", modulecode_win32com$client$gencache, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"win32com.client.genpy", modulecode_win32com$client$genpy, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"win32com.client.makepy", modulecode_win32com$client$makepy, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"win32com.client.selecttlb", modulecode_win32com$client$selecttlb, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"win32com.client.util", modulecode_win32com$client$util, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"win32con", modulecode_win32con, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"winerror", modulecode_winerror, 0, 0, NUITKA_TRANSLATED_FLAG},
    {NULL, NULL, 0, 0, 0}
};

static void _loadBytesCodesBlob()
{
    static bool init_done = false;

    if (init_done == false) {
        loadConstantsBlob((PyObject **)bytecode_data, ".bytecode");

        init_done = true;
    }
}


void setupMetaPathBasedLoader(void) {
    static bool init_done = false;
    if (init_done == false) {
        _loadBytesCodesBlob();
        registerMetaPathBasedUnfreezer(meta_path_loader_entries, bytecode_data);

        init_done = true;
    }


}

// This provides the frozen (compiled bytecode) files that are included if
// any.

// These modules should be loaded as bytecode. They may e.g. have to be loadable
// during "Py_Initialize" already, or for irrelevance, they are only included
// in this un-optimized form. These are not compiled by Nuitka, and therefore
// are not accelerated at all, merely bundled with the binary or module, so
// that CPython library can start out finding them.

struct frozen_desc {
    char const *name;
    int index;
    int size;
};

static struct frozen_desc _frozen_modules[] = {

    {NULL, 0, 0}
};


void copyFrozenModulesTo(struct _frozen *destination) {
    _loadBytesCodesBlob();

    struct frozen_desc *current = _frozen_modules;

    for (;;) {
        destination->name = (char *)current->name;
        destination->code = bytecode_data[current->index];
        destination->size = current->size;

        if (destination->name == NULL) break;

        current += 1;
        destination += 1;
    };
}


