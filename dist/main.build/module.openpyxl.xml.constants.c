/* Generated code for Python module 'openpyxl.xml.constants'
 * created by Nuitka version 0.6.15.3
 *
 * This code is in part copyright 2021 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "nuitka/unfreezing.h"

#include "__helpers.h"

/* The "module_openpyxl$xml$constants" is a Python object pointer of module type.
 *
 * Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_openpyxl$xml$constants;
PyDictObject *moduledict_openpyxl$xml$constants;

/* The declarations of module constants used, if any. */
static PyObject *mod_consts[155];

static PyObject *module_filename_obj = NULL;

/* Indicator if this modules private constants were created yet. */
static bool constants_created = false;

/* Function to create module private constants. */
static void createModuleConstants(void) {
    if (constants_created == false) {
        loadConstantsBlob(&mod_consts[0], UNTRANSLATE("openpyxl.xml.constants"));
        constants_created = true;
    }
}

/* For multiprocessing, we want to be able to initialize the __main__ constants. */
#if (_NUITKA_PLUGIN_MULTIPROCESSING_ENABLED || _NUITKA_PLUGIN_TRACEBACK_ENCRYPTION_ENABLED) && 0
void createMainModuleConstants(void) {
    createModuleConstants();
}
#endif

/* Function to verify module private constants for non-corruption. */
#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_openpyxl$xml$constants(void) {
    // The module may not have been used at all, then ignore this.
    if (constants_created == false) return;

    checkConstantsBlob(&mod_consts[0], "openpyxl.xml.constants");
}
#endif

// The module code objects.
static PyCodeObject *codeobj_fe3b80a17b075f3b0f13fb8e3886812f;

static void createModuleCodeObjects(void) {
    module_filename_obj = MAKE_RELATIVE_PATH(mod_consts[153]); CHECK_OBJECT(module_filename_obj);
    codeobj_fe3b80a17b075f3b0f13fb8e3886812f = MAKE_CODEOBJECT(module_filename_obj, 1, CO_NOFREE, mod_consts[154], NULL, NULL, 0, 0, 0);
}

// The module function declarations.


// The module function definitions.


extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();

extern PyTypeObject Nuitka_Loader_Type;

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
// Provide a way to create find a function via its C code and create it back
// in another process, useful for multiprocessing extensions like dill
extern void registerDillPluginTables(char const *module_name, PyMethodDef *reduce_compiled_function, PyMethodDef *create_compiled_function);

function_impl_code functable_openpyxl$xml$constants[] = {

    NULL
};

static char const *_reduce_compiled_function_argnames[] = {
    "func",
    NULL
};

static PyObject *_reduce_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    PyObject *func;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:reduce_compiled_function", (char **)_reduce_compiled_function_argnames, &func, NULL)) {
        return NULL;
    }

    if (Nuitka_Function_Check(func) == false) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "not a compiled function");
        return NULL;
    }

    struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)func;

    function_impl_code *current = functable_openpyxl$xml$constants;
    int offset = 0;

    while (*current != NULL) {
        if (*current == function->m_c_code) {
            break;
        }

        current += 1;
        offset += 1;
    }

    if (*current == NULL) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "Cannot find compiled function in module.");
        return NULL;
    }

    PyObject *code_object_desc = PyTuple_New(6);
    PyTuple_SET_ITEM0(code_object_desc, 0, function->m_code_object->co_filename);
    PyTuple_SET_ITEM0(code_object_desc, 1, function->m_code_object->co_name);
    PyTuple_SET_ITEM(code_object_desc, 2, PyLong_FromLong(function->m_code_object->co_firstlineno));
    PyTuple_SET_ITEM0(code_object_desc, 3, function->m_code_object->co_varnames);
    PyTuple_SET_ITEM(code_object_desc, 4, PyLong_FromLong(function->m_code_object->co_argcount));
    PyTuple_SET_ITEM(code_object_desc, 5, PyLong_FromLong(function->m_code_object->co_flags));

    CHECK_OBJECT_DEEP(code_object_desc);

    PyObject *result = PyTuple_New(4);
    PyTuple_SET_ITEM(result, 0, PyLong_FromLong(offset));
    PyTuple_SET_ITEM(result, 1, code_object_desc);
    PyTuple_SET_ITEM0(result, 2, function->m_defaults);
    PyTuple_SET_ITEM0(result, 3, function->m_doc != NULL ? function->m_doc : Py_None);

    CHECK_OBJECT_DEEP(result);

    return result;
}

static PyMethodDef _method_def_reduce_compiled_function = {"reduce_compiled_function", (PyCFunction)_reduce_compiled_function,
                                                           METH_VARARGS | METH_KEYWORDS, NULL};

static char const *_create_compiled_function_argnames[] = {
    "func",
    "code_object_desc",
    "defaults",
    "doc",
    NULL
};


static PyObject *_create_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    CHECK_OBJECT_DEEP(args);

    PyObject *func;
    PyObject *code_object_desc;
    PyObject *defaults;
    PyObject *doc;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOOO:create_compiled_function", (char **)_create_compiled_function_argnames, &func, &code_object_desc, &defaults, &doc, NULL)) {
        return NULL;
    }

    int offset = PyLong_AsLong(func);

    if (offset == -1 && ERROR_OCCURRED()) {
        return NULL;
    }

    if (offset > sizeof(functable_openpyxl$xml$constants) || offset < 0) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "Wrong offset for compiled function.");
        return NULL;
    }

    PyObject *filename = PyTuple_GET_ITEM(code_object_desc, 0);
    PyObject *function_name = PyTuple_GET_ITEM(code_object_desc, 1);
    PyObject *line = PyTuple_GET_ITEM(code_object_desc, 2);
    int line_int = PyLong_AsLong(line);
    assert(!ERROR_OCCURRED());

    PyObject *argnames = PyTuple_GET_ITEM(code_object_desc, 3);
    PyObject *arg_count = PyTuple_GET_ITEM(code_object_desc, 4);
    int arg_count_int = PyLong_AsLong(arg_count);
    assert(!ERROR_OCCURRED());
    PyObject *flags = PyTuple_GET_ITEM(code_object_desc, 5);
    int flags_int = PyLong_AsLong(flags);
    assert(!ERROR_OCCURRED());

    PyCodeObject *code_object = MAKE_CODEOBJECT(
        filename,
        line_int,
        flags_int,
        function_name,
        argnames,
        NULL, // freevars
        arg_count_int,
        0, // TODO: Missing kw_only_count
        0 // TODO: Missing pos_only_count
    );

    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        functable_openpyxl$xml$constants[offset],
        code_object->co_name,
#if PYTHON_VERSION >= 0x300
        NULL, // TODO: Not transferring qualname yet
#endif
        code_object,
        defaults,
#if PYTHON_VERSION >= 0x300
        NULL, // kwdefaults are done on the outside currently
        NULL, // TODO: Not transferring annotations
#endif
        module_openpyxl$xml$constants,
        doc,
        NULL,
        0
    );

    return (PyObject *)result;
}

static PyMethodDef _method_def_create_compiled_function = {
    "create_compiled_function",
    (PyCFunction)_create_compiled_function,
    METH_VARARGS | METH_KEYWORDS, NULL
};


#endif

// Internal entry point for module code.
PyObject *modulecode_openpyxl$xml$constants(PyObject *module, struct Nuitka_MetaPathBasedLoaderEntry const *module_entry) {
    module_openpyxl$xml$constants = module;

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    /* Initialize the compiled types of Nuitka. */
    _initCompiledCellType();
    _initCompiledGeneratorType();
    _initCompiledFunctionType();
    _initCompiledMethodType();
    _initCompiledFrameType();

#if PYTHON_VERSION < 0x300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 0x270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

    // Enable meta path based loader if not already done.
#ifdef _NUITKA_TRACE
    PRINT_STRING("openpyxl.xml.constants: Calling setupMetaPathBasedLoader().\n");
#endif
    setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 0x300
    patchInspectModule();
#endif

#endif

    /* The constants only used by this module are created now. */
#ifdef _NUITKA_TRACE
    PRINT_STRING("openpyxl.xml.constants: Calling createModuleConstants().\n");
#endif
    createModuleConstants();

    /* The code objects used by this module are created now. */
#ifdef _NUITKA_TRACE
    PRINT_STRING("openpyxl.xml.constants: Calling createModuleCodeObjects().\n");
#endif
    createModuleCodeObjects();

    // PRINT_STRING("in initopenpyxl$xml$constants\n");

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.

    moduledict_openpyxl$xml$constants = MODULE_DICT(module_openpyxl$xml$constants);

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
    registerDillPluginTables(module_entry->name, &_method_def_reduce_compiled_function, &_method_def_create_compiled_function);
#endif

    // Set "__compiled__" to what version information we have.
    UPDATE_STRING_DICT0(
        moduledict_openpyxl$xml$constants,
        (Nuitka_StringObject *)const_str_plain___compiled__,
        Nuitka_dunder_compiled_value
    );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        UPDATE_STRING_DICT0(
            moduledict_openpyxl$xml$constants,
            (Nuitka_StringObject *)const_str_plain___package__,
            const_str_empty
        );
#elif 0
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)const_str_plain___name__);

        UPDATE_STRING_DICT0(
            moduledict_openpyxl$xml$constants,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 0x300
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)const_str_plain___name__);
        char const *module_name_cstr = PyString_AS_STRING(module_name);

        char const *last_dot = strrchr(module_name_cstr, '.');

        if (last_dot != NULL) {
            UPDATE_STRING_DICT1(
                moduledict_openpyxl$xml$constants,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize(module_name_cstr, last_dot - module_name_cstr)
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)const_str_plain___name__);
        Py_ssize_t dot_index = PyUnicode_Find(module_name, const_str_dot, 0, PyUnicode_GetLength(module_name), -1);

        if (dot_index != -1) {
            UPDATE_STRING_DICT1(
                moduledict_openpyxl$xml$constants,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring(module_name, 0, dot_index)
            );
        }
#endif
#endif
    }

    CHECK_OBJECT(module_openpyxl$xml$constants);

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if (GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)const_str_plain___builtins__) == NULL) {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if !defined(_NUITKA_EXE) || !0
        value = PyModule_GetDict(value);
#endif

        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)const_str_plain___builtins__, value);
    }

#if PYTHON_VERSION >= 0x300
    UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type);
#endif

#if PYTHON_VERSION >= 0x340
// Set the "__spec__" value

#if 0
    // Main modules just get "None" as spec.
    UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)const_str_plain___spec__, Py_None);
#else
    // Other modules get a "ModuleSpec" from the standard mechanism.
    {
        PyObject *bootstrap_module = getImportLibBootstrapModule();
        CHECK_OBJECT(bootstrap_module);

        PyObject *_spec_from_module = PyObject_GetAttrString(bootstrap_module, "_spec_from_module");
        CHECK_OBJECT(_spec_from_module);

        PyObject *spec_value = CALL_FUNCTION_WITH_SINGLE_ARG(_spec_from_module, module_openpyxl$xml$constants);
        Py_DECREF(_spec_from_module);

        // We can assume this to never fail, or else we are in trouble anyway.
        // CHECK_OBJECT(spec_value);

        if (spec_value == NULL) {
            PyErr_PrintEx(0);
            abort();
        }

// Mark the execution in the "__spec__" value.
        SET_ATTRIBUTE(spec_value, const_str_plain__initializing, Py_True);

        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)const_str_plain___spec__, spec_value);
    }
#endif
#endif

    // Temp variables if any
    struct Nuitka_FrameObject *frame_fe3b80a17b075f3b0f13fb8e3886812f;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    bool tmp_result;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    int tmp_res;

    // Module code.
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = mod_consts[0];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[1], tmp_assign_source_1);
    }
    {
        PyObject *tmp_assign_source_2;
        tmp_assign_source_2 = module_filename_obj;
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[2], tmp_assign_source_2);
    }
    // Frame without reuse.
    frame_fe3b80a17b075f3b0f13fb8e3886812f = MAKE_MODULE_FRAME(codeobj_fe3b80a17b075f3b0f13fb8e3886812f, module_openpyxl$xml$constants);

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack(frame_fe3b80a17b075f3b0f13fb8e3886812f);
    assert(Py_REFCNT(frame_fe3b80a17b075f3b0f13fb8e3886812f) == 2);

    // Framed code:
    {
        PyObject *tmp_assattr_name_1;
        PyObject *tmp_assattr_target_1;
        tmp_assattr_name_1 = module_filename_obj;
        tmp_assattr_target_1 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[3]);

        if (unlikely(tmp_assattr_target_1 == NULL)) {
            tmp_assattr_target_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[3]);
        }

        assert(!(tmp_assattr_target_1 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_1, mod_consts[4], tmp_assattr_name_1);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assattr_name_2;
        PyObject *tmp_assattr_target_2;
        tmp_assattr_name_2 = Py_True;
        tmp_assattr_target_2 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[3]);

        if (unlikely(tmp_assattr_target_2 == NULL)) {
            tmp_assattr_target_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[3]);
        }

        assert(!(tmp_assattr_target_2 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_2, mod_consts[5], tmp_assattr_name_2);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assign_source_3;
        tmp_assign_source_3 = Py_None;
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[6], tmp_assign_source_3);
    }
    {
        PyObject *tmp_assign_source_4;
        tmp_assign_source_4 = mod_consts[7];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[8], tmp_assign_source_4);
    }
    {
        PyObject *tmp_assign_source_5;
        tmp_assign_source_5 = mod_consts[7];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[9], tmp_assign_source_5);
    }
    {
        PyObject *tmp_assign_source_6;
        tmp_assign_source_6 = mod_consts[10];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[11], tmp_assign_source_6);
    }
    {
        PyObject *tmp_assign_source_7;
        tmp_assign_source_7 = mod_consts[12];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[13], tmp_assign_source_7);
    }
    {
        PyObject *tmp_assign_source_8;
        tmp_assign_source_8 = mod_consts[14];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[15], tmp_assign_source_8);
    }
    {
        PyObject *tmp_assign_source_9;
        tmp_assign_source_9 = mod_consts[16];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17], tmp_assign_source_9);
    }
    {
        PyObject *tmp_assign_source_10;
        tmp_assign_source_10 = mod_consts[18];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[19], tmp_assign_source_10);
    }
    {
        PyObject *tmp_assign_source_11;
        PyObject *tmp_left_name_1;
        PyObject *tmp_left_name_2;
        PyObject *tmp_right_name_1;
        PyObject *tmp_right_name_2;
        tmp_left_name_2 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_left_name_2 == NULL)) {
            tmp_left_name_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[17]);
        }

        assert(!(tmp_left_name_2 == NULL));
        tmp_right_name_1 = mod_consts[20];
        tmp_left_name_1 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_2, tmp_right_name_1);
        assert(!(tmp_left_name_1 == NULL));
        tmp_right_name_2 = mod_consts[21];
        tmp_assign_source_11 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_1, tmp_right_name_2);
        Py_DECREF(tmp_left_name_1);
        assert(!(tmp_assign_source_11 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[22], tmp_assign_source_11);
    }
    {
        PyObject *tmp_assign_source_12;
        PyObject *tmp_left_name_3;
        PyObject *tmp_left_name_4;
        PyObject *tmp_right_name_3;
        PyObject *tmp_right_name_4;
        tmp_left_name_4 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_left_name_4 == NULL)) {
            tmp_left_name_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[17]);
        }

        assert(!(tmp_left_name_4 == NULL));
        tmp_right_name_3 = mod_consts[20];
        tmp_left_name_3 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_4, tmp_right_name_3);
        assert(!(tmp_left_name_3 == NULL));
        tmp_right_name_4 = mod_consts[23];
        tmp_assign_source_12 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_3, tmp_right_name_4);
        Py_DECREF(tmp_left_name_3);
        assert(!(tmp_assign_source_12 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[24], tmp_assign_source_12);
    }
    {
        PyObject *tmp_assign_source_13;
        PyObject *tmp_left_name_5;
        PyObject *tmp_left_name_6;
        PyObject *tmp_right_name_5;
        PyObject *tmp_right_name_6;
        tmp_left_name_6 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_left_name_6 == NULL)) {
            tmp_left_name_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[17]);
        }

        assert(!(tmp_left_name_6 == NULL));
        tmp_right_name_5 = mod_consts[20];
        tmp_left_name_5 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_6, tmp_right_name_5);
        assert(!(tmp_left_name_5 == NULL));
        tmp_right_name_6 = mod_consts[25];
        tmp_assign_source_13 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_5, tmp_right_name_6);
        Py_DECREF(tmp_left_name_5);
        assert(!(tmp_assign_source_13 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[26], tmp_assign_source_13);
    }
    {
        PyObject *tmp_assign_source_14;
        PyObject *tmp_left_name_7;
        PyObject *tmp_left_name_8;
        PyObject *tmp_right_name_7;
        PyObject *tmp_right_name_8;
        tmp_left_name_8 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_left_name_8 == NULL)) {
            tmp_left_name_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[17]);
        }

        assert(!(tmp_left_name_8 == NULL));
        tmp_right_name_7 = mod_consts[20];
        tmp_left_name_7 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_8, tmp_right_name_7);
        assert(!(tmp_left_name_7 == NULL));
        tmp_right_name_8 = mod_consts[27];
        tmp_assign_source_14 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_7, tmp_right_name_8);
        Py_DECREF(tmp_left_name_7);
        assert(!(tmp_assign_source_14 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[28], tmp_assign_source_14);
    }
    {
        PyObject *tmp_assign_source_15;
        PyObject *tmp_left_name_9;
        PyObject *tmp_left_name_10;
        PyObject *tmp_right_name_9;
        PyObject *tmp_right_name_10;
        tmp_left_name_10 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_left_name_10 == NULL)) {
            tmp_left_name_10 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[17]);
        }

        assert(!(tmp_left_name_10 == NULL));
        tmp_right_name_9 = mod_consts[20];
        tmp_left_name_9 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_10, tmp_right_name_9);
        assert(!(tmp_left_name_9 == NULL));
        tmp_right_name_10 = mod_consts[29];
        tmp_assign_source_15 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_9, tmp_right_name_10);
        Py_DECREF(tmp_left_name_9);
        assert(!(tmp_assign_source_15 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[30], tmp_assign_source_15);
    }
    {
        PyObject *tmp_assign_source_16;
        PyObject *tmp_left_name_11;
        PyObject *tmp_left_name_12;
        PyObject *tmp_right_name_11;
        PyObject *tmp_right_name_12;
        tmp_left_name_12 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_left_name_12 == NULL)) {
            tmp_left_name_12 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[17]);
        }

        assert(!(tmp_left_name_12 == NULL));
        tmp_right_name_11 = mod_consts[20];
        tmp_left_name_11 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_12, tmp_right_name_11);
        assert(!(tmp_left_name_11 == NULL));
        tmp_right_name_12 = mod_consts[31];
        tmp_assign_source_16 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_11, tmp_right_name_12);
        Py_DECREF(tmp_left_name_11);
        assert(!(tmp_assign_source_16 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[32], tmp_assign_source_16);
    }
    {
        PyObject *tmp_assign_source_17;
        PyObject *tmp_left_name_13;
        PyObject *tmp_left_name_14;
        PyObject *tmp_right_name_13;
        PyObject *tmp_right_name_14;
        tmp_left_name_14 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[24]);

        if (unlikely(tmp_left_name_14 == NULL)) {
            tmp_left_name_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[24]);
        }

        assert(!(tmp_left_name_14 == NULL));
        tmp_right_name_13 = mod_consts[20];
        tmp_left_name_13 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_14, tmp_right_name_13);
        assert(!(tmp_left_name_13 == NULL));
        tmp_right_name_14 = mod_consts[18];
        tmp_assign_source_17 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_13, tmp_right_name_14);
        Py_DECREF(tmp_left_name_13);
        assert(!(tmp_assign_source_17 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[33], tmp_assign_source_17);
    }
    {
        PyObject *tmp_assign_source_18;
        PyObject *tmp_left_name_15;
        PyObject *tmp_left_name_16;
        PyObject *tmp_right_name_15;
        PyObject *tmp_right_name_16;
        tmp_left_name_16 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[26]);

        if (unlikely(tmp_left_name_16 == NULL)) {
            tmp_left_name_16 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[26]);
        }

        assert(!(tmp_left_name_16 == NULL));
        tmp_right_name_15 = mod_consts[20];
        tmp_left_name_15 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_16, tmp_right_name_15);
        assert(!(tmp_left_name_15 == NULL));
        tmp_right_name_16 = mod_consts[18];
        tmp_assign_source_18 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_15, tmp_right_name_16);
        Py_DECREF(tmp_left_name_15);
        assert(!(tmp_assign_source_18 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[34], tmp_assign_source_18);
    }
    {
        PyObject *tmp_assign_source_19;
        PyObject *tmp_left_name_17;
        PyObject *tmp_left_name_18;
        PyObject *tmp_right_name_17;
        PyObject *tmp_right_name_18;
        tmp_left_name_18 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_left_name_18 == NULL)) {
            tmp_left_name_18 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[17]);
        }

        assert(!(tmp_left_name_18 == NULL));
        tmp_right_name_17 = mod_consts[20];
        tmp_left_name_17 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_18, tmp_right_name_17);
        assert(!(tmp_left_name_17 == NULL));
        tmp_right_name_18 = mod_consts[35];
        tmp_assign_source_19 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_17, tmp_right_name_18);
        Py_DECREF(tmp_left_name_17);
        assert(!(tmp_assign_source_19 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[36], tmp_assign_source_19);
    }
    {
        PyObject *tmp_assign_source_20;
        PyObject *tmp_left_name_19;
        PyObject *tmp_left_name_20;
        PyObject *tmp_right_name_19;
        PyObject *tmp_right_name_20;
        tmp_left_name_20 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_left_name_20 == NULL)) {
            tmp_left_name_20 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[17]);
        }

        assert(!(tmp_left_name_20 == NULL));
        tmp_right_name_19 = mod_consts[20];
        tmp_left_name_19 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_20, tmp_right_name_19);
        assert(!(tmp_left_name_19 == NULL));
        tmp_right_name_20 = mod_consts[37];
        tmp_assign_source_20 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_19, tmp_right_name_20);
        Py_DECREF(tmp_left_name_19);
        assert(!(tmp_assign_source_20 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[38], tmp_assign_source_20);
    }
    {
        PyObject *tmp_assign_source_21;
        tmp_assign_source_21 = mod_consts[39];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[40], tmp_assign_source_21);
    }
    {
        PyObject *tmp_assign_source_22;
        PyObject *tmp_left_name_21;
        PyObject *tmp_right_name_21;
        tmp_left_name_21 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[19]);

        if (unlikely(tmp_left_name_21 == NULL)) {
            tmp_left_name_21 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[19]);
        }

        assert(!(tmp_left_name_21 == NULL));
        tmp_right_name_21 = mod_consts[41];
        tmp_assign_source_22 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_21, tmp_right_name_21);
        assert(!(tmp_assign_source_22 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[42], tmp_assign_source_22);
    }
    {
        PyObject *tmp_assign_source_23;
        PyObject *tmp_left_name_22;
        PyObject *tmp_left_name_23;
        PyObject *tmp_left_name_24;
        PyObject *tmp_right_name_22;
        PyObject *tmp_right_name_23;
        PyObject *tmp_right_name_24;
        tmp_left_name_24 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_left_name_24 == NULL)) {
            tmp_left_name_24 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[17]);
        }

        assert(!(tmp_left_name_24 == NULL));
        tmp_right_name_22 = mod_consts[20];
        tmp_left_name_23 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_24, tmp_right_name_22);
        assert(!(tmp_left_name_23 == NULL));
        tmp_right_name_23 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[19]);

        if (unlikely(tmp_right_name_23 == NULL)) {
            tmp_right_name_23 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[19]);
        }

        assert(!(tmp_right_name_23 == NULL));
        tmp_left_name_22 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_23, tmp_right_name_23);
        Py_DECREF(tmp_left_name_23);
        assert(!(tmp_left_name_22 == NULL));
        tmp_right_name_24 = mod_consts[43];
        tmp_assign_source_23 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_22, tmp_right_name_24);
        Py_DECREF(tmp_left_name_22);
        assert(!(tmp_assign_source_23 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[44], tmp_assign_source_23);
    }
    {
        PyObject *tmp_assign_source_24;
        PyObject *tmp_left_name_25;
        PyObject *tmp_right_name_25;
        tmp_left_name_25 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[15]);

        if (unlikely(tmp_left_name_25 == NULL)) {
            tmp_left_name_25 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[15]);
        }

        assert(!(tmp_left_name_25 == NULL));
        tmp_right_name_25 = mod_consts[45];
        tmp_assign_source_24 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_25, tmp_right_name_25);
        assert(!(tmp_assign_source_24 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[46], tmp_assign_source_24);
    }
    {
        PyObject *tmp_assign_source_25;
        PyObject *tmp_left_name_26;
        PyObject *tmp_right_name_26;
        tmp_left_name_26 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[15]);

        if (unlikely(tmp_left_name_26 == NULL)) {
            tmp_left_name_26 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[15]);
        }

        assert(!(tmp_left_name_26 == NULL));
        tmp_right_name_26 = mod_consts[47];
        tmp_assign_source_25 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_26, tmp_right_name_26);
        assert(!(tmp_assign_source_25 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[48], tmp_assign_source_25);
    }
    {
        PyObject *tmp_assign_source_26;
        PyObject *tmp_left_name_27;
        PyObject *tmp_right_name_27;
        tmp_left_name_27 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_left_name_27 == NULL)) {
            tmp_left_name_27 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[17]);
        }

        assert(!(tmp_left_name_27 == NULL));
        tmp_right_name_27 = mod_consts[49];
        tmp_assign_source_26 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_27, tmp_right_name_27);
        assert(!(tmp_assign_source_26 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[50], tmp_assign_source_26);
    }
    {
        PyObject *tmp_assign_source_27;
        PyObject *tmp_left_name_28;
        PyObject *tmp_right_name_28;
        tmp_left_name_28 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_left_name_28 == NULL)) {
            tmp_left_name_28 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[17]);
        }

        assert(!(tmp_left_name_28 == NULL));
        tmp_right_name_28 = mod_consts[51];
        tmp_assign_source_27 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_28, tmp_right_name_28);
        assert(!(tmp_assign_source_27 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[52], tmp_assign_source_27);
    }
    {
        PyObject *tmp_assign_source_28;
        PyObject *tmp_left_name_29;
        PyObject *tmp_right_name_29;
        tmp_left_name_29 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[22]);

        if (unlikely(tmp_left_name_29 == NULL)) {
            tmp_left_name_29 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[22]);
        }

        assert(!(tmp_left_name_29 == NULL));
        tmp_right_name_29 = mod_consts[53];
        tmp_assign_source_28 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_29, tmp_right_name_29);
        assert(!(tmp_assign_source_28 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[54], tmp_assign_source_28);
    }
    {
        PyObject *tmp_assign_source_29;
        PyObject *tmp_left_name_30;
        PyObject *tmp_right_name_30;
        tmp_left_name_30 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_left_name_30 == NULL)) {
            tmp_left_name_30 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[17]);
        }

        assert(!(tmp_left_name_30 == NULL));
        tmp_right_name_30 = mod_consts[55];
        tmp_assign_source_29 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_30, tmp_right_name_30);
        assert(!(tmp_assign_source_29 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[56], tmp_assign_source_29);
    }
    {
        PyObject *tmp_assign_source_30;
        tmp_assign_source_30 = mod_consts[57];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[58], tmp_assign_source_30);
    }
    {
        PyObject *tmp_assign_source_31;
        tmp_assign_source_31 = mod_consts[59];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[60], tmp_assign_source_31);
    }
    {
        PyObject *tmp_assign_source_32;
        tmp_assign_source_32 = mod_consts[61];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[62], tmp_assign_source_32);
    }
    {
        PyObject *tmp_assign_source_33;
        tmp_assign_source_33 = mod_consts[63];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[64], tmp_assign_source_33);
    }
    {
        PyObject *tmp_assign_source_34;
        tmp_assign_source_34 = mod_consts[65];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[66], tmp_assign_source_34);
    }
    {
        PyObject *tmp_assign_source_35;
        tmp_assign_source_35 = mod_consts[67];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[68], tmp_assign_source_35);
    }
    {
        PyObject *tmp_assign_source_36;
        PyObject *tmp_left_name_31;
        PyObject *tmp_right_name_31;
        tmp_left_name_31 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[68]);

        if (unlikely(tmp_left_name_31 == NULL)) {
            tmp_left_name_31 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[68]);
        }

        assert(!(tmp_left_name_31 == NULL));
        tmp_right_name_31 = mod_consts[69];
        tmp_assign_source_36 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_31, tmp_right_name_31);
        assert(!(tmp_assign_source_36 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[70], tmp_assign_source_36);
    }
    {
        PyObject *tmp_assign_source_37;
        PyObject *tmp_left_name_32;
        PyObject *tmp_right_name_32;
        tmp_left_name_32 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[70]);

        if (unlikely(tmp_left_name_32 == NULL)) {
            tmp_left_name_32 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[70]);
        }

        assert(!(tmp_left_name_32 == NULL));
        tmp_right_name_32 = mod_consts[71];
        tmp_assign_source_37 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_32, tmp_right_name_32);
        assert(!(tmp_assign_source_37 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[72], tmp_assign_source_37);
    }
    {
        PyObject *tmp_assign_source_38;
        PyObject *tmp_left_name_33;
        PyObject *tmp_right_name_33;
        tmp_left_name_33 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[70]);

        if (unlikely(tmp_left_name_33 == NULL)) {
            tmp_left_name_33 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[70]);
        }

        assert(!(tmp_left_name_33 == NULL));
        tmp_right_name_33 = mod_consts[73];
        tmp_assign_source_38 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_33, tmp_right_name_33);
        assert(!(tmp_assign_source_38 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[74], tmp_assign_source_38);
    }
    {
        PyObject *tmp_assign_source_39;
        PyObject *tmp_left_name_34;
        PyObject *tmp_right_name_34;
        tmp_left_name_34 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[70]);

        if (unlikely(tmp_left_name_34 == NULL)) {
            tmp_left_name_34 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[70]);
        }

        assert(!(tmp_left_name_34 == NULL));
        tmp_right_name_34 = mod_consts[75];
        tmp_assign_source_39 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_34, tmp_right_name_34);
        assert(!(tmp_assign_source_39 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[76], tmp_assign_source_39);
    }
    {
        PyObject *tmp_assign_source_40;
        PyObject *tmp_left_name_35;
        PyObject *tmp_right_name_35;
        tmp_left_name_35 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[68]);

        if (unlikely(tmp_left_name_35 == NULL)) {
            tmp_left_name_35 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[68]);
        }

        assert(!(tmp_left_name_35 == NULL));
        tmp_right_name_35 = mod_consts[77];
        tmp_assign_source_40 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_35, tmp_right_name_35);
        assert(!(tmp_assign_source_40 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[78], tmp_assign_source_40);
    }
    {
        PyObject *tmp_assign_source_41;
        PyObject *tmp_left_name_36;
        PyObject *tmp_right_name_36;
        tmp_left_name_36 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[68]);

        if (unlikely(tmp_left_name_36 == NULL)) {
            tmp_left_name_36 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[68]);
        }

        assert(!(tmp_left_name_36 == NULL));
        tmp_right_name_36 = mod_consts[79];
        tmp_assign_source_41 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_36, tmp_right_name_36);
        assert(!(tmp_assign_source_41 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[80], tmp_assign_source_41);
    }
    {
        PyObject *tmp_assign_source_42;
        PyObject *tmp_left_name_37;
        PyObject *tmp_right_name_37;
        tmp_left_name_37 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[70]);

        if (unlikely(tmp_left_name_37 == NULL)) {
            tmp_left_name_37 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[70]);
        }

        assert(!(tmp_left_name_37 == NULL));
        tmp_right_name_37 = mod_consts[81];
        tmp_assign_source_42 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_37, tmp_right_name_37);
        assert(!(tmp_assign_source_42 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[82], tmp_assign_source_42);
    }
    {
        PyObject *tmp_assign_source_43;
        tmp_assign_source_43 = mod_consts[83];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[84], tmp_assign_source_43);
    }
    {
        PyObject *tmp_assign_source_44;
        PyObject *tmp_left_name_38;
        PyObject *tmp_right_name_38;
        tmp_left_name_38 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[84]);

        if (unlikely(tmp_left_name_38 == NULL)) {
            tmp_left_name_38 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[84]);
        }

        assert(!(tmp_left_name_38 == NULL));
        tmp_right_name_38 = mod_consts[69];
        tmp_assign_source_44 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_38, tmp_right_name_38);
        assert(!(tmp_assign_source_44 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[85], tmp_assign_source_44);
    }
    {
        PyObject *tmp_assign_source_45;
        PyObject *tmp_left_name_39;
        PyObject *tmp_right_name_39;
        tmp_left_name_39 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[84]);

        if (unlikely(tmp_left_name_39 == NULL)) {
            tmp_left_name_39 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[84]);
        }

        assert(!(tmp_left_name_39 == NULL));
        tmp_right_name_39 = mod_consts[86];
        tmp_assign_source_45 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_39, tmp_right_name_39);
        assert(!(tmp_assign_source_45 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[87], tmp_assign_source_45);
    }
    {
        PyObject *tmp_assign_source_46;
        PyObject *tmp_left_name_40;
        PyObject *tmp_right_name_40;
        tmp_left_name_40 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[84]);

        if (unlikely(tmp_left_name_40 == NULL)) {
            tmp_left_name_40 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[84]);
        }

        assert(!(tmp_left_name_40 == NULL));
        tmp_right_name_40 = mod_consts[88];
        tmp_assign_source_46 = BINARY_OPERATION_ADD_OBJECT_UNICODE_UNICODE(tmp_left_name_40, tmp_right_name_40);
        assert(!(tmp_assign_source_46 == NULL));
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[89], tmp_assign_source_46);
    }
    {
        PyObject *tmp_assign_source_47;
        tmp_assign_source_47 = mod_consts[90];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[91], tmp_assign_source_47);
    }
    {
        PyObject *tmp_assign_source_48;
        tmp_assign_source_48 = mod_consts[59];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[60], tmp_assign_source_48);
    }
    {
        PyObject *tmp_assign_source_49;
        tmp_assign_source_49 = mod_consts[92];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[93], tmp_assign_source_49);
    }
    {
        PyObject *tmp_assign_source_50;
        tmp_assign_source_50 = mod_consts[94];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[95], tmp_assign_source_50);
    }
    {
        PyObject *tmp_assign_source_51;
        tmp_assign_source_51 = mod_consts[96];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[97], tmp_assign_source_51);
    }
    {
        PyObject *tmp_assign_source_52;
        tmp_assign_source_52 = mod_consts[98];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[99], tmp_assign_source_52);
    }
    {
        PyObject *tmp_assign_source_53;
        tmp_assign_source_53 = mod_consts[100];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[101], tmp_assign_source_53);
    }
    {
        PyObject *tmp_assign_source_54;
        tmp_assign_source_54 = mod_consts[102];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[103], tmp_assign_source_54);
    }
    {
        PyObject *tmp_assign_source_55;
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[104];
        tmp_dict_value_1 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[87]);

        if (unlikely(tmp_dict_value_1 == NULL)) {
            tmp_dict_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[87]);
        }

        assert(!(tmp_dict_value_1 == NULL));
        tmp_assign_source_55 = _PyDict_NewPresized( 8 );
        tmp_res = PyDict_SetItem(tmp_assign_source_55, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[105];
        tmp_dict_value_1 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[62]);

        if (unlikely(tmp_dict_value_1 == NULL)) {
            tmp_dict_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[62]);
        }

        assert(!(tmp_dict_value_1 == NULL));
        tmp_res = PyDict_SetItem(tmp_assign_source_55, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[66]);

        if (unlikely(tmp_dict_key_1 == NULL)) {
            tmp_dict_key_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[66]);
        }

        assert(!(tmp_dict_key_1 == NULL));
        tmp_dict_value_1 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[64]);

        if (unlikely(tmp_dict_value_1 == NULL)) {
            tmp_dict_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[64]);
        }

        assert(!(tmp_dict_value_1 == NULL));
        tmp_res = PyDict_SetItem(tmp_assign_source_55, tmp_dict_key_1, tmp_dict_value_1);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 74;

            goto dict_build_exception_1;
        }
        tmp_dict_key_1 = mod_consts[106];
        tmp_dict_value_1 = mod_consts[107];
        tmp_res = PyDict_SetItem(tmp_assign_source_55, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[108];
        tmp_dict_value_1 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[91]);

        if (unlikely(tmp_dict_value_1 == NULL)) {
            tmp_dict_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[91]);
        }

        assert(!(tmp_dict_value_1 == NULL));
        tmp_res = PyDict_SetItem(tmp_assign_source_55, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[109];
        tmp_dict_value_1 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[78]);

        if (unlikely(tmp_dict_value_1 == NULL)) {
            tmp_dict_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[78]);
        }

        assert(!(tmp_dict_value_1 == NULL));
        tmp_res = PyDict_SetItem(tmp_assign_source_55, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[110];
        tmp_dict_value_1 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[60]);

        if (unlikely(tmp_dict_value_1 == NULL)) {
            tmp_dict_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[60]);
        }

        assert(!(tmp_dict_value_1 == NULL));
        tmp_res = PyDict_SetItem(tmp_assign_source_55, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[111];
        tmp_dict_value_1 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[93]);

        if (unlikely(tmp_dict_value_1 == NULL)) {
            tmp_dict_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[93]);
        }

        assert(!(tmp_dict_value_1 == NULL));
        tmp_res = PyDict_SetItem(tmp_assign_source_55, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto dict_build_noexception_1;
        // Exception handling pass through code for dict_build:
        dict_build_exception_1:;
        Py_DECREF(tmp_assign_source_55);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_1:;
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[112], tmp_assign_source_55);
    }
    {
        PyObject *tmp_assign_source_56;
        tmp_assign_source_56 = mod_consts[113];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[114], tmp_assign_source_56);
    }
    {
        PyObject *tmp_assign_source_57;
        tmp_assign_source_57 = mod_consts[115];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[116], tmp_assign_source_57);
    }
    {
        PyObject *tmp_assign_source_58;
        tmp_assign_source_58 = mod_consts[117];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[118], tmp_assign_source_58);
    }
    {
        PyObject *tmp_assign_source_59;
        PyObject *tmp_left_name_41;
        PyObject *tmp_right_name_41;
        tmp_left_name_41 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[118]);

        if (unlikely(tmp_left_name_41 == NULL)) {
            tmp_left_name_41 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[118]);
        }

        assert(!(tmp_left_name_41 == NULL));
        tmp_right_name_41 = mod_consts[119];
        tmp_assign_source_59 = BINARY_OPERATION_MOD_OBJECT_UNICODE_UNICODE(tmp_left_name_41, tmp_right_name_41);
        if (tmp_assign_source_59 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 89;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[120], tmp_assign_source_59);
    }
    {
        PyObject *tmp_assign_source_60;
        PyObject *tmp_left_name_42;
        PyObject *tmp_right_name_42;
        tmp_left_name_42 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[118]);

        if (unlikely(tmp_left_name_42 == NULL)) {
            tmp_left_name_42 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[118]);
        }

        if (tmp_left_name_42 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 90;

            goto frame_exception_exit_1;
        }
        tmp_right_name_42 = mod_consts[121];
        tmp_assign_source_60 = BINARY_OPERATION_MOD_OBJECT_OBJECT_UNICODE(tmp_left_name_42, tmp_right_name_42);
        if (tmp_assign_source_60 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 90;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[122], tmp_assign_source_60);
    }
    {
        PyObject *tmp_assign_source_61;
        PyObject *tmp_left_name_43;
        PyObject *tmp_right_name_43;
        tmp_left_name_43 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[118]);

        if (unlikely(tmp_left_name_43 == NULL)) {
            tmp_left_name_43 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[118]);
        }

        if (tmp_left_name_43 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 91;

            goto frame_exception_exit_1;
        }
        tmp_right_name_43 = mod_consts[123];
        tmp_assign_source_61 = BINARY_OPERATION_MOD_OBJECT_OBJECT_UNICODE(tmp_left_name_43, tmp_right_name_43);
        if (tmp_assign_source_61 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 91;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[124], tmp_assign_source_61);
    }
    {
        PyObject *tmp_assign_source_62;
        PyObject *tmp_left_name_44;
        PyObject *tmp_right_name_44;
        tmp_left_name_44 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[118]);

        if (unlikely(tmp_left_name_44 == NULL)) {
            tmp_left_name_44 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[118]);
        }

        if (tmp_left_name_44 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 92;

            goto frame_exception_exit_1;
        }
        tmp_right_name_44 = mod_consts[125];
        tmp_assign_source_62 = BINARY_OPERATION_MOD_OBJECT_OBJECT_UNICODE(tmp_left_name_44, tmp_right_name_44);
        if (tmp_assign_source_62 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 92;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[126], tmp_assign_source_62);
    }
    {
        PyObject *tmp_assign_source_63;
        PyObject *tmp_left_name_45;
        PyObject *tmp_right_name_45;
        tmp_left_name_45 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[118]);

        if (unlikely(tmp_left_name_45 == NULL)) {
            tmp_left_name_45 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[118]);
        }

        if (tmp_left_name_45 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 93;

            goto frame_exception_exit_1;
        }
        tmp_right_name_45 = mod_consts[127];
        tmp_assign_source_63 = BINARY_OPERATION_MOD_OBJECT_OBJECT_UNICODE(tmp_left_name_45, tmp_right_name_45);
        if (tmp_assign_source_63 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 93;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[128], tmp_assign_source_63);
    }
    {
        PyObject *tmp_assign_source_64;
        PyObject *tmp_left_name_46;
        PyObject *tmp_right_name_46;
        tmp_left_name_46 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[118]);

        if (unlikely(tmp_left_name_46 == NULL)) {
            tmp_left_name_46 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[118]);
        }

        if (tmp_left_name_46 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 94;

            goto frame_exception_exit_1;
        }
        tmp_right_name_46 = mod_consts[129];
        tmp_assign_source_64 = BINARY_OPERATION_MOD_OBJECT_OBJECT_UNICODE(tmp_left_name_46, tmp_right_name_46);
        if (tmp_assign_source_64 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 94;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[130], tmp_assign_source_64);
    }
    {
        PyObject *tmp_assign_source_65;
        tmp_assign_source_65 = mod_consts[131];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[132], tmp_assign_source_65);
    }
    {
        PyObject *tmp_assign_source_66;
        tmp_assign_source_66 = mod_consts[133];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[134], tmp_assign_source_66);
    }
    {
        PyObject *tmp_assign_source_67;
        tmp_assign_source_67 = mod_consts[135];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[136], tmp_assign_source_67);
    }
    {
        PyObject *tmp_assign_source_68;
        tmp_assign_source_68 = mod_consts[137];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[138], tmp_assign_source_68);
    }
    {
        PyObject *tmp_assign_source_69;
        PyObject *tmp_left_name_47;
        PyObject *tmp_right_name_47;
        tmp_left_name_47 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[114]);

        if (unlikely(tmp_left_name_47 == NULL)) {
            tmp_left_name_47 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[114]);
        }

        if (tmp_left_name_47 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 99;

            goto frame_exception_exit_1;
        }
        tmp_right_name_47 = mod_consts[139];
        tmp_assign_source_69 = BINARY_OPERATION_MOD_OBJECT_OBJECT_UNICODE(tmp_left_name_47, tmp_right_name_47);
        if (tmp_assign_source_69 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 99;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[140], tmp_assign_source_69);
    }
    {
        PyObject *tmp_assign_source_70;
        PyObject *tmp_left_name_48;
        PyObject *tmp_right_name_48;
        tmp_left_name_48 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[114]);

        if (unlikely(tmp_left_name_48 == NULL)) {
            tmp_left_name_48 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[114]);
        }

        if (tmp_left_name_48 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 100;

            goto frame_exception_exit_1;
        }
        tmp_right_name_48 = mod_consts[141];
        tmp_assign_source_70 = BINARY_OPERATION_MOD_OBJECT_OBJECT_UNICODE(tmp_left_name_48, tmp_right_name_48);
        if (tmp_assign_source_70 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 100;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[142], tmp_assign_source_70);
    }
    {
        PyObject *tmp_assign_source_71;
        PyObject *tmp_left_name_49;
        PyObject *tmp_right_name_49;
        tmp_left_name_49 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[116]);

        if (unlikely(tmp_left_name_49 == NULL)) {
            tmp_left_name_49 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[116]);
        }

        if (tmp_left_name_49 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 101;

            goto frame_exception_exit_1;
        }
        tmp_right_name_49 = mod_consts[139];
        tmp_assign_source_71 = BINARY_OPERATION_MOD_OBJECT_OBJECT_UNICODE(tmp_left_name_49, tmp_right_name_49);
        if (tmp_assign_source_71 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 101;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[143], tmp_assign_source_71);
    }
    {
        PyObject *tmp_assign_source_72;
        PyObject *tmp_left_name_50;
        PyObject *tmp_right_name_50;
        tmp_left_name_50 = GET_STRING_DICT_VALUE(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[116]);

        if (unlikely(tmp_left_name_50 == NULL)) {
            tmp_left_name_50 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[116]);
        }

        if (tmp_left_name_50 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 102;

            goto frame_exception_exit_1;
        }
        tmp_right_name_50 = mod_consts[141];
        tmp_assign_source_72 = BINARY_OPERATION_MOD_OBJECT_OBJECT_UNICODE(tmp_left_name_50, tmp_right_name_50);
        if (tmp_assign_source_72 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 102;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[144], tmp_assign_source_72);
    }

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION(frame_fe3b80a17b075f3b0f13fb8e3886812f);
#endif
    popFrameStack();

    assertFrameObject(frame_fe3b80a17b075f3b0f13fb8e3886812f);

    goto frame_no_exception_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION(frame_fe3b80a17b075f3b0f13fb8e3886812f);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_fe3b80a17b075f3b0f13fb8e3886812f, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_fe3b80a17b075f3b0f13fb8e3886812f->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_fe3b80a17b075f3b0f13fb8e3886812f, exception_lineno);
    }

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto module_exception_exit;

    frame_no_exception_1:;
    {
        PyObject *tmp_assign_source_73;
        tmp_assign_source_73 = PyDict_Copy(mod_consts[145]);
        UPDATE_STRING_DICT1(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[146], tmp_assign_source_73);
    }
    {
        PyObject *tmp_assign_source_74;
        tmp_assign_source_74 = mod_consts[147];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[148], tmp_assign_source_74);
    }
    {
        PyObject *tmp_assign_source_75;
        tmp_assign_source_75 = mod_consts[149];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[150], tmp_assign_source_75);
    }
    {
        PyObject *tmp_assign_source_76;
        tmp_assign_source_76 = mod_consts[151];
        UPDATE_STRING_DICT0(moduledict_openpyxl$xml$constants, (Nuitka_StringObject *)mod_consts[152], tmp_assign_source_76);
    }

    return module_openpyxl$xml$constants;
    module_exception_exit:
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);
    return NULL;
}

