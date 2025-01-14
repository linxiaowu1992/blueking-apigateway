// Code generated by MockGen. DO NOT EDIT.
// Source: app_gateway_permission.go

// Package mock is a generated GoMock package.
package mock

import (
	dao "core/pkg/database/dao"
	reflect "reflect"

	gomock "github.com/golang/mock/gomock"
)

// MockAppGatewayPermissionManager is a mock of AppGatewayPermissionManager interface.
type MockAppGatewayPermissionManager struct {
	ctrl     *gomock.Controller
	recorder *MockAppGatewayPermissionManagerMockRecorder
}

// MockAppGatewayPermissionManagerMockRecorder is the mock recorder for MockAppGatewayPermissionManager.
type MockAppGatewayPermissionManagerMockRecorder struct {
	mock *MockAppGatewayPermissionManager
}

// NewMockAppGatewayPermissionManager creates a new mock instance.
func NewMockAppGatewayPermissionManager(ctrl *gomock.Controller) *MockAppGatewayPermissionManager {
	mock := &MockAppGatewayPermissionManager{ctrl: ctrl}
	mock.recorder = &MockAppGatewayPermissionManagerMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use.
func (m *MockAppGatewayPermissionManager) EXPECT() *MockAppGatewayPermissionManagerMockRecorder {
	return m.recorder
}

// Get mocks base method.
func (m *MockAppGatewayPermissionManager) Get(bkAppCode string, gatewayID int64) (dao.AppGatewayPermission, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "Get", bkAppCode, gatewayID)
	ret0, _ := ret[0].(dao.AppGatewayPermission)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// Get indicates an expected call of Get.
func (mr *MockAppGatewayPermissionManagerMockRecorder) Get(bkAppCode, gatewayID interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "Get", reflect.TypeOf((*MockAppGatewayPermissionManager)(nil).Get), bkAppCode, gatewayID)
}
