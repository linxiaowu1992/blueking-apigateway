// Code generated by MockGen. DO NOT EDIT.
// Source: public_key.go

// Package mock is a generated GoMock package.
package mock

import (
	reflect "reflect"

	gomock "github.com/golang/mock/gomock"
)

// MockGatewayPublicKeyService is a mock of GatewayPublicKeyService interface.
type MockGatewayPublicKeyService struct {
	ctrl     *gomock.Controller
	recorder *MockGatewayPublicKeyServiceMockRecorder
}

// MockGatewayPublicKeyServiceMockRecorder is the mock recorder for MockGatewayPublicKeyService.
type MockGatewayPublicKeyServiceMockRecorder struct {
	mock *MockGatewayPublicKeyService
}

// NewMockGatewayPublicKeyService creates a new mock instance.
func NewMockGatewayPublicKeyService(ctrl *gomock.Controller) *MockGatewayPublicKeyService {
	mock := &MockGatewayPublicKeyService{ctrl: ctrl}
	mock.recorder = &MockGatewayPublicKeyServiceMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use.
func (m *MockGatewayPublicKeyService) EXPECT() *MockGatewayPublicKeyServiceMockRecorder {
	return m.recorder
}

// Get mocks base method.
func (m *MockGatewayPublicKeyService) Get(instanceID, gatewayName string) (string, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "Get", instanceID, gatewayName)
	ret0, _ := ret[0].(string)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// Get indicates an expected call of Get.
func (mr *MockGatewayPublicKeyServiceMockRecorder) Get(instanceID, gatewayName interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "Get", reflect.TypeOf((*MockGatewayPublicKeyService)(nil).Get), instanceID, gatewayName)
}